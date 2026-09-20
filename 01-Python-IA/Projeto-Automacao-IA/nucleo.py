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


def precisa_de_acao_humana(sentimento: str) -> bool:
    """Decide se uma classificacao precisa virar uma acao pendente.

    Regra da Semana 2 (Volume 2): feedback negativo sempre precisa de
    alguem olhando — e o "agir" depois do "decidir".
    """
    return sentimento.strip().lower() == "negativo"


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
