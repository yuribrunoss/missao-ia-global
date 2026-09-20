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
    criar_acao_pendente,
    errors,
    inicializar_banco,
    montar_cliente,
    obter_acoes_pendentes,
    obter_historico,
    parsear_resposta,
    precisa_de_acao_humana,
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


def mostrar_acoes_pendentes(limite: int = 20) -> None:
    """Imprime as acoes pendentes (feedbacks negativos que precisam de atencao)."""
    acoes = obter_acoes_pendentes(limite)

    if not acoes:
        print("\nNenhuma acao pendente no momento.\n")
        return

    print(f"\n=== {len(acoes)} acao(oes) pendente(s) ===")
    for acao in acoes:
        feedback = acao["feedback"]
        resumo = feedback if len(feedback) <= 60 else feedback[:57] + "..."
        print(f"- [{acao['criado_em']}] {resumo}")
        print(f"  motivo: {acao['motivo']}")
    print()


def main() -> None:
    print("=== Classificador de Feedbacks com IA ===")
    print("Digite um feedback de cliente e pressione Enter.")
    print("Digite 'historico' para ver as ultimas classificacoes salvas.")
    print("Digite 'acoes' para ver as acoes pendentes (feedbacks negativos).")
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

        if feedback.lower() == "acoes":
            mostrar_acoes_pendentes()
            continue

        if not feedback:
            print("Digite algum texto antes de continuar.\n")
            continue

        try:
            resultado = classificar_feedback(client, feedback)
            print("\n" + resultado.strip() + "\n")

            sentimento, justificativa, resposta_sugerida = parsear_resposta(resultado)
            classificacao_id = salvar_no_historico(
                feedback, sentimento, justificativa, resposta_sugerida
            )

            if precisa_de_acao_humana(sentimento):
                criar_acao_pendente(
                    classificacao_id,
                    "Feedback negativo — revisar e responder ao cliente.",
                )
                print("(sentimento negativo: acao pendente criada — digite 'acoes' pra ver)\n")
        except errors.APIError as erro:
            print(f"\nDeu erro ao chamar a API: {erro}\n")


if __name__ == "__main__":
    main()
