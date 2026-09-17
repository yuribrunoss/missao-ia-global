"""
Classificador de Feedbacks com IA
==================================

Semana 1 do Projeto de Automacao com IA (Missao IA Global).

O que esse script faz:
1. Pede pra voce colar um feedback de cliente (texto livre).
2. Manda esse texto pra API do Gemini.
3. A IA responde com: sentimento (positivo / negativo / neutro) e uma
   justificativa curta.
4. Mostra o resultado na tela.

Conceitos praticados aqui: variavel de ambiente (.env), chamada de API,
tratamento basico de erro, laco de repeticao (loop) no terminal.
"""

import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import errors

# Carrega as variaveis do arquivo .env (onde fica a chave da API)
load_dotenv()

MODELO = "gemini-3.6-flash"

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


def main() -> None:
    print("=== Classificador de Feedbacks com IA ===")
    print("Digite um feedback de cliente e pressione Enter.")
    print("Digite 'sair' para encerrar.\n")

    client = montar_cliente()

    while True:
        feedback = input("Feedback: ").strip()

        if feedback.lower() == "sair":
            print("Ate a proxima!")
            break

        if not feedback:
            print("Digite algum texto antes de continuar.\n")
            continue

        try:
            resultado = classificar_feedback(client, feedback)
            print("\n" + resultado.strip() + "\n")

        except errors.APIError as erro:
            print(f"\nDeu erro ao chamar a API: {erro}\n")


if __name__ == "__main__":
    main()
