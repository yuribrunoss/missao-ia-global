"""
Nucleo compartilhado do Projeto de Automacao com IA
=====================================================

Toda a logica que tanto o CLI (classificador.py) quanto a API (api.py)
usam: montar o cliente da IA, classificar um feedback, interpretar a
resposta e guardar/ler o historico no SQLite.

Nenhum dos dois pontos de entrada (CLI ou API) deve duplicar essa
logica — os dois so importam daqui.
"""

import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import (
    errors,  # noqa: F401 - reexportado p/ api.py e classificador.py capturarem errors.APIError
    types,
)

load_dotenv()

MODELO = "gemini-3.6-flash"
BANCO_DE_DADOS = Path(__file__).parent / "historico.db"

PROMPT_BASE = """Voce e um assistente que analisa feedbacks de clientes e sugere como responder a eles.

Leia o feedback abaixo e responda EXATAMENTE neste formato:

Sentimento: <positivo, negativo ou neutro>
Justificativa: <uma frase curta explicando o motivo>
Resposta sugerida: <uma resposta curta e educada para enviar ao cliente, coerente com o sentimento>

Feedback do cliente:
\"\"\"{feedback}\"\"\"
"""

# Volume 3: em vez de um "if sentimento == negativo" fixo no Python, o
# Gemini recebe essa ferramenta e decide ELE MESMO se deve cham a-la.
FERRAMENTA_CRIAR_ACAO_PENDENTE = types.FunctionDeclaration(
    name="criar_acao_pendente",
    description=(
        "Chame esta funcao quando esse feedback precisar que alguem da "
        "equipe revise e responda ao cliente (tipicamente feedback "
        "negativo ou uma reclamacao seria). Nao chame para feedbacks "
        "positivos ou neutros sem problema real."
    ),
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "motivo": types.Schema(
                type=types.Type.STRING,
                description=(
                    "Breve motivo pelo qual esse feedback precisa de "
                    "atencao humana."
                ),
            ),
        },
        required=["motivo"],
    ),
)

PROMPT_DECISAO_AGENTE = """Voce e um agente que decide se um feedback de cliente, ja classificado, precisa de atencao humana.

Feedback do cliente:
\"\"\"{feedback}\"\"\"

Sentimento identificado: {sentimento}
Justificativa: {justificativa}

Se esse caso precisar que alguem da equipe revise e responda ao cliente, chame a funcao criar_acao_pendente explicando o motivo. Se nao precisar (feedback positivo ou neutro sem problema), responda apenas "Nenhuma acao necessaria." sem chamar nenhuma funcao.
"""


class ChaveNaoConfigurada(RuntimeError):
    """Erro levantado quando a GOOGLE_API_KEY nao esta configurada."""


def montar_cliente() -> genai.Client:
    """Cria o cliente da API do Gemini usando a chave do .env."""
    chave = os.getenv("GOOGLE_API_KEY")

    if not chave or chave == "coloque_sua_chave_aqui":
        raise ChaveNaoConfigurada(
            "GOOGLE_API_KEY nao configurada.\n"
            "1. Copie o arquivo .env.example para .env\n"
            "2. Pegue sua chave gratis em https://aistudio.google.com/apikey\n"
            "3. Cole a chave no arquivo .env"
        )

    return genai.Client(api_key=chave)


def classificar_feedback(client: genai.Client, feedback: str) -> str:
    """Envia o feedback para a IA e retorna a classificacao em texto."""
    prompt = PROMPT_BASE.format(feedback=feedback)

    resposta = client.models.generate_content(
        model=MODELO,
        contents=prompt,
    )

    return resposta.text or "Sem resposta da IA"


def decidir_acao_com_agente(
    client: genai.Client, feedback: str, sentimento: str, justificativa: str
) -> str | None:
    """Deixa o Gemini decidir, via function calling, se esse caso precisa
    virar uma acao pendente — em vez de uma regra fixa no Python.

    Retorna o motivo (string) se o agente decidiu que precisa de acao, ou
    None se ele decidiu que nao precisa.
    """
    prompt = PROMPT_DECISAO_AGENTE.format(
        feedback=feedback, sentimento=sentimento, justificativa=justificativa
    )

    resposta = client.models.generate_content(
        model=MODELO,
        contents=prompt,
        config=types.GenerateContentConfig(
            tools=[
                types.Tool(function_declarations=[FERRAMENTA_CRIAR_ACAO_PENDENTE])
            ],
        ),
    )

    chamadas = resposta.function_calls or []
    for chamada in chamadas:
        if chamada.name == "criar_acao_pendente":
            args = chamada.args or {}
            return args.get("motivo") or "Feedback requer atencao humana."

    return None


def parsear_resposta(resposta: str) -> tuple[str, str, str]:
    """Extrai sentimento, justificativa e resposta sugerida do texto que a IA devolveu."""
    sentimento = ""
    justificativa = ""
    resposta_sugerida = ""

    for linha in resposta.splitlines():
        linha = linha.strip()
        if linha.lower().startswith("sentimento:"):
            sentimento = linha.split(":", 1)[1].strip()
        elif linha.lower().startswith("justificativa:"):
            justificativa = linha.split(":", 1)[1].strip()
        elif linha.lower().startswith("resposta sugerida:"):
            resposta_sugerida = linha.split(":", 1)[1].strip()

    return sentimento, justificativa, resposta_sugerida


def inicializar_banco() -> None:
    """Cria a tabela de historico se ainda nao existir (e migra bancos antigos)."""
    with sqlite3.connect(BANCO_DE_DADOS) as conexao:
        conexao.execute(
            """
            CREATE TABLE IF NOT EXISTS classificacoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                feedback TEXT NOT NULL,
                sentimento TEXT,
                justificativa TEXT,
                resposta_sugerida TEXT,
                criado_em TEXT NOT NULL
            )
            """
        )

        # Migracao: bancos criados antes da Semana 1 do Volume 2 nao tem
        # essa coluna ainda. Adiciona sem perder o historico existente.
        colunas = {
            linha[1] for linha in conexao.execute("PRAGMA table_info(classificacoes)")
        }
        if "resposta_sugerida" not in colunas:
            conexao.execute(
                "ALTER TABLE classificacoes ADD COLUMN resposta_sugerida TEXT"
            )

        conexao.execute(
            """
            CREATE TABLE IF NOT EXISTS acoes_pendentes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                classificacao_id INTEGER NOT NULL,
                motivo TEXT NOT NULL,
                criado_em TEXT NOT NULL,
                FOREIGN KEY (classificacao_id) REFERENCES classificacoes (id)
            )
            """
        )


def salvar_no_historico(
    feedback: str, sentimento: str, justificativa: str, resposta_sugerida: str
) -> int:
    """Guarda uma classificacao no banco SQLite local e retorna o id gerado."""
    with sqlite3.connect(BANCO_DE_DADOS) as conexao:
        cursor = conexao.execute(
            "INSERT INTO classificacoes "
            "(feedback, sentimento, justificativa, resposta_sugerida, criado_em) "
            "VALUES (?, ?, ?, ?, ?)",
            (
                feedback,
                sentimento,
                justificativa,
                resposta_sugerida,
                datetime.now(timezone.utc).isoformat(),
            ),
        )
        return cursor.lastrowid


def obter_historico(limite: int = 5) -> list[dict]:
    """Retorna as ultimas classificacoes salvas, mais recente primeiro."""
    with sqlite3.connect(BANCO_DE_DADOS) as conexao:
        linhas = conexao.execute(
            "SELECT feedback, sentimento, justificativa, resposta_sugerida, criado_em "
            "FROM classificacoes ORDER BY id DESC LIMIT ?",
            (limite,),
        ).fetchall()

    return [
        {
            "feedback": feedback,
            "sentimento": sentimento,
            "justificativa": justificativa,
            "resposta_sugerida": resposta_sugerida,
            "criado_em": criado_em,
        }
        for feedback, sentimento, justificativa, resposta_sugerida, criado_em in linhas
    ]


def criar_acao_pendente(classificacao_id: int, motivo: str) -> None:
    """Registra que uma classificacao precisa de atencao humana."""
    with sqlite3.connect(BANCO_DE_DADOS) as conexao:
        conexao.execute(
            "INSERT INTO acoes_pendentes (classificacao_id, motivo, criado_em) "
            "VALUES (?, ?, ?)",
            (classificacao_id, motivo, datetime.now(timezone.utc).isoformat()),
        )


def obter_acoes_pendentes(limite: int = 20) -> list[dict]:
    """Retorna as acoes pendentes mais recentes, com o feedback original."""
    with sqlite3.connect(BANCO_DE_DADOS) as conexao:
        linhas = conexao.execute(
            """
            SELECT acoes_pendentes.id,
                   acoes_pendentes.motivo,
                   acoes_pendentes.criado_em,
                   classificacoes.feedback,
                   classificacoes.sentimento,
                   classificacoes.resposta_sugerida
            FROM acoes_pendentes
            JOIN classificacoes ON classificacoes.id = acoes_pendentes.classificacao_id
            ORDER BY acoes_pendentes.id DESC
            LIMIT ?
            """,
            (limite,),
        ).fetchall()

    return [
        {
            "id": id_,
            "motivo": motivo,
            "criado_em": criado_em,
            "feedback": feedback,
            "sentimento": sentimento,
            "resposta_sugerida": resposta_sugerida,
        }
        for id_, motivo, criado_em, feedback, sentimento, resposta_sugerida in linhas
    ]
