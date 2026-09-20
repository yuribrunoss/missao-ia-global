"""
API de Automacao com IA (FastAPI)
====================================

Semana 2 do Projeto de Automacao com IA (Missao IA Global).

Expoe a mesma logica do classificador.py como uma API HTTP: qualquer
sistema (nao so uma pessoa digitando no terminal) pode mandar um
feedback e receber a classificacao de volta.

Para rodar:
    uv run uvicorn api:app --reload

Depois abra http://127.0.0.1:8000/docs no navegador pra testar de
forma interativa (o FastAPI gera essa pagina sozinho).
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

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

_cliente = None


@asynccontextmanager
async def gerenciar_ciclo_de_vida(app: FastAPI):
    """Roda uma vez quando a API sobe: cria o cliente da IA e o banco."""
    global _cliente

    try:
        _cliente = montar_cliente()
    except ChaveNaoConfigurada as erro:
        raise RuntimeError(str(erro)) from erro

    inicializar_banco()

    yield  # a API fica no ar aqui

    # nada pra limpar quando a API encerra


app = FastAPI(
    title="Classificador de Feedbacks com IA",
    description="Classifica o sentimento de feedbacks de clientes usando a API do Gemini.",
    version="0.3.0",
    lifespan=gerenciar_ciclo_de_vida,
)


@app.get("/", include_in_schema=False)
def raiz() -> RedirectResponse:
    """Redireciona a raiz da API para a documentacao interativa (/docs)."""
    return RedirectResponse(url="/docs")


class FeedbackEntrada(BaseModel):
    feedback: str


class ClassificacaoSaida(BaseModel):
    sentimento: str
    justificativa: str
    resposta_sugerida: str
    resposta_completa: str


@app.post("/classificar", response_model=ClassificacaoSaida)
def classificar(entrada: FeedbackEntrada) -> ClassificacaoSaida:
    """Recebe um feedback de cliente e devolve a classificacao de sentimento."""
    feedback = entrada.feedback.strip()

    if not feedback:
        raise HTTPException(
            status_code=400, detail="O campo 'feedback' nao pode estar vazio."
        )

    try:
        resultado = classificar_feedback(_cliente, feedback)
    except errors.APIError as erro:
        raise HTTPException(
            status_code=502, detail=f"Erro ao chamar a API do Gemini: {erro}"
        ) from erro

    sentimento, justificativa, resposta_sugerida = parsear_resposta(resultado)
    salvar_no_historico(feedback, sentimento, justificativa, resposta_sugerida)

    return ClassificacaoSaida(
        sentimento=sentimento,
        justificativa=justificativa,
        resposta_sugerida=resposta_sugerida,
        resposta_completa=resultado.strip(),
    )


@app.get("/historico")
def historico(limite: int = 5) -> list[dict]:
    """Retorna as ultimas classificacoes salvas."""
    return obter_historico(limite)
