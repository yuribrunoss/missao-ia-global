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

PROMPT_BASE = """Voce e um assistente que analisa feedbacks de clientes.

Leia o feedback abaixo e responda EXATAMENTE neste formato:

Sentimento: <positivo, negativo ou neutro>
Justificativa: <uma frase curta explicando o motivo>

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


def parsear_resposta(resposta: str) -> tuple[str, str]:
    """Extrai sentimento e justificativa do texto que a IA devolveu."""
    sentimento = ""
    justificativa = ""

    for linha in resposta.splitlines():
        linha = linha.strip()
        if linha.lower().startswith("sentimento:"):
            sentimento = linha.split(":", 1)[1].strip()
        elif linha.lower().startswith("justificativa:"):
            justificativa = linha.split(":", 1)[1].strip()

    return sentimento, justificativa


def inicializar_banco() -> None:
    """Cria a tabela de historico se ainda nao existir."""
    with sqlite3.connect(BANCO_DE_DADOS) as conexao:
        conexao.execute(
            """
            CREATE TABLE IF NOT EXISTS classificacoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                feedback TEXT NOT NULL,
                sentimento TEXT,
                justificativa TEXT,
                criado_em TEXT NOT NULL
            )
            """
        )


def salvar_no_historico(feedback: str, sentimento: str, justificativa: str) -> None:
    """Guarda uma classificacao no banco SQLite local."""
    with sqlite3.connect(BANCO_DE_DADOS) as conexao:
        conexao.execute(
            "INSERT INTO classificacoes (feedback, sentimento, justificativa, criado_em) "
            "VALUES (?, ?, ?, ?)",
            (feedback, sentimento, justificativa, datetime.now(timezone.utc).isoformat()),
        )


def obter_historico(limite: int = 5) -> list[dict]:
    """Retorna as ultimas classificacoes salvas, mais recente primeiro."""
    with sqlite3.connect(BANCO_DE_DADOS) as conexao:
        linhas = conexao.execute(
            "SELECT feedback, sentimento, justificativa, criado_em "
            "FROM classificacoes ORDER BY id DESC LIMIT ?",
            (limite,),
        ).fetchall()

    return [
        {
            "feedback": feedback,
            "sentimento": sentimento,
            "justificativa": justificativa,
            "criado_em": criado_em,
        }
        for feedback, sentimento, justificativa, criado_em in linhas
    ]
