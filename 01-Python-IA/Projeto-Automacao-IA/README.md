# Projeto de Automação com IA — Semana 1

Primeiro passo do projeto prático da Missão IA Global: em vez de um ERP
inteiro, um pedaço pequeno e real de **automação com IA**, que evolui
semana a semana.

## O que ele faz hoje (Semana 1)

Um script de terminal que recebe um feedback de cliente (texto livre) e
usa a API do Gemini para classificar o sentimento — positivo, negativo ou
neutro — com uma justificativa curta.

Problema de negócio que representa: qualquer empresa que recebe muito
feedback de cliente (suporte, avaliações, redes sociais) precisa triar
isso rápido antes de decidir o que responder primeiro. Esse script é a
semente disso.

## Como rodar

1. Tenha o [uv](https://docs.astral.sh/uv/) instalado (você já usa ele no
   Volume 0).
2. Copie `.env.example` para `.env`:
   ```bash
   cp .env.example .env
   ```
3. Pegue uma chave grátis da API do Gemini em
   https://aistudio.google.com/apikey (não precisa cartão de crédito) e
   cole no `.env`, no lugar de `coloque_sua_chave_aqui`.
4. Instale as dependências:
   ```bash
   uv sync
   ```
5. Rode:
   ```bash
   uv run classificador.py
   ```
6. Digite um feedback, veja a classificação. Digite `sair` para encerrar.

## Próximas semanas (plano)

- **Semana 2:** guardar o histórico de classificações em SQLite/CSV e
  expor essa mesma lógica como uma API com FastAPI.
- **Semana 3:** tratamento de erro mais robusto e deploy grátis (Render/
  Railway/Fly.io).
- **Semana 4:** README final, link no GitHub e primeiro post no LinkedIn
  mostrando o projeto rodando.

Plano completo em `claude/plano-4-semanas.md` no projeto Missão IA
Global.
