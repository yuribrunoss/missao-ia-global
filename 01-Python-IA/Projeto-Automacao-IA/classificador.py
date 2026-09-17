"""
Classificador de Feedbacks com IA
==================================

Semana 1 e 2 do Projeto de Automacao com IA (Missao IA Global).

O que esse script faz:
1. Pede pra voce colar um feedback de cliente (texto livre).
2. Manda esse texto pra API do Gemini.
3. A IA responde com: sentimento (positivo / negativo / neutro) e uma
   justificativa curta.
4. Mostra o resultado na tela e guarda no historico (banco SQLite local).
5. Digitando "historico", mostra as ultimas classificacoes salvas.

Conceitos praticados aqui: variavel de ambiente (.env), chamada de API,
tratamento de erro especifico, laco de repeticao (loop), banco de dados
SQLite (persistencia).
"""

import os
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import errors

# Carrega as variaveis do arquivo .env (onde fica a chave da API)
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


def montar_cliente() -> genai.Client:
    """Cria o cliente da API do Gemini usando a chave do .env."""
    chave = os.getenv("GOOGLE_API_KEY")

    if not chave or chave == "coloque_sua_chave_aqui":
        print(
            "Nao encontrei a GOOGLE_API_KEY configurada.\n"
            "1. Copie o arquivo .env.example para .env\n"
            "2. Pegue sua chave gratis em https://aistudio.google.com/apikey\n"
            "3. Cole a chave no arquivo .env\n"
        )
        sys.exit(1)

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


def mostrar_historico(limite: int = 5) -> None:
    """Mostra as ultimas classificacoes salvas no banco."""
    with sqlite3.connect(BANCO_DE_DADOS) as conexao:
        linhas = conexao.execute(
            "SELECT feedback, sentimento, justificativa, criado_em "
            "FROM classificacoes ORDER BY id DESC LIMIT ?",
            (limite,),
        ).fetchall()

    if not linhas:
        print("\nAinda nao ha nada no historico.\n")
        return

    print(f"\n=== Ultimas {len(linhas)} classificacoes ===")
    for feedback, sentimento, justificativa, criado_em in linhas:
        resumo = feedback if len(feedback) <= 60 else feedback[:57] + "..."
        print(f"- [{criado_em}] {sentimento}: {resumo}")
        print(f"  motivo: {justificativa}")
    print()


def main() -> None:
    print("=== Classificador de Feedbacks com IA ===")
    print("Digite um feedback de cliente e pressione Enter.")
    print("Digite 'historico' para ver as ultimas classificacoes salvas.")
    print("Digite 'sair' para encerrar.\n")

    client = montar_cliente()
    inicializar_banco()

    while True:
        feedback = input("Feedback: ").strip()

        if feedback.lower() == "sair":
            print("Ate a proxima!")
            break

        if feedback.lower() == "historico":
            mostrar_historico()
            continue

        if not feedback:
            print("Digite algum texto antes de continuar.\n")
            continue

        try:
            resultado = classificar_feedback(client, feedback)
            print("\n" + resultado.strip() + "\n")

            sentimento, justificativa = parsear_resposta(resultado)
            salvar_no_historico(feedback, sentimento, justificativa)
        except errors.APIError as erro:
            print(f"\nDeu erro ao chamar a API: {erro}\n")


if __name__ == "__main__":
    main()
