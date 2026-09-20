"""
Classificador de Feedbacks com IA (CLI)
=========================================

Semana 1 e 2 do Projeto de Automacao com IA (Missao IA Global).

O que esse script faz:
1. Pede pra voce colar um feedback de cliente (texto livre).
2. Manda esse texto pra API do Gemini.
3. A IA responde com: sentimento (positivo / negativo / neutro) e uma
   justificativa curta.
4. Mostra o resultado na tela e guarda no historico (banco SQLite local).
5. Digitando "historico", mostra as ultimas classificacoes salvas.

A logica de verdade (chamar a IA, interpretar a resposta, guardar no
banco) mora em nucleo.py — esse arquivo aqui e so a "casca" de terminal.
A api.py usa a mesma logica, so que exposta como API HTTP.
"""

import sys

from nucleo import (
    ChaveNaoConfigurada,
    classificar_feedback,
    errors,
    inicializar_banco,
    montar_cliente,
    obter_historico,
    parsear_resposta,
    salvar_no_historico,
)


def mostrar_historico(limite: int = 5) -> None:
    """Imprime as ultimas classificacoes salvas no banco."""
    registros = obter_historico(limite)

    if not registros:
        print("\nAinda nao ha nada no historico.\n")
        return

    print(f"\n=== Ultimas {len(registros)} classificacoes ===")
    for registro in registros:
        feedback = registro["feedback"]
        resumo = feedback if len(feedback) <= 60 else feedback[:57] + "..."
        print(f"- [{registro['criado_em']}] {registro['sentimento']}: {resumo}")
        print(f"  motivo: {registro['justificativa']}")
        print(f"  resposta sugerida: {registro['resposta_sugerida']}")
    print()


def main() -> None:
    print("=== Classificador de Feedbacks com IA ===")
    print("Digite um feedback de cliente e pressione Enter.")
    print("Digite 'historico' para ver as ultimas classificacoes salvas.")
    print("Digite 'sair' para encerrar.\n")

    try:
        client = montar_cliente()
    except ChaveNaoConfigurada as erro:
        print(f"\n{erro}\n")
        sys.exit(1)

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

            sentimento, justificativa, resposta_sugerida = parsear_resposta(resultado)
            salvar_no_historico(feedback, sentimento, justificativa, resposta_sugerida)
        except errors.APIError as erro:
            print(f"\nDeu erro ao chamar a API: {erro}\n")


if __name__ == "__main__":
    main()
