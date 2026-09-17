# Projeto de Automação com IA — Semana 2

Projeto prático da Missão IA Global: automação com IA que evolui semana a
semana.

## O que ele faz hoje

Um script de terminal que recebe um feedback de cliente (texto livre),
usa a API do Gemini para classificar o sentimento — positivo, negativo
ou neutro — com justificativa, e agora também **guarda esse histórico**
num banco SQLite local (`historico.db`, não vai pro git). Digite
`historico` a qualquer momento pra ver as últimas classificações
salvas.

Problema de negócio que representa: qualquer empresa que recebe muito
feedback de cliente (suporte, avaliações, redes sociais) precisa triar
isso rápido e manter um registro de como os clientes estão se sentindo
ao longo do tempo.

## Como rodar

1. Tenha o [uv](https://docs.astral.sh/uv/) instalado.
2. Copie `.env.example` para `.env`:
   ```bash
   cp .env.example .env
   ```
3. Pegue uma chave grátis da API do Gemini em
   https://aistudio.google.com/apikey e cole no `.env`.
4. Instale as dependências:
   ```bash
   uv sync
   ```
5. Rode:
   ```bash
   uv run classificador.py
   ```
6. Digite um feedback e veja a classificação. Digite `historico` pra
   ver o que já foi salvo. Digite `sair` para encerrar.

## Próximas etapas (plano)

- **Ainda na Semana 2:** expor essa mesma lógica como uma API com
  FastAPI (1-2 endpoints, ex.: `POST /classificar`).
- **Semana 3:** tratamento de erro mais robusto e deploy grátis (Render/
  Railway/Fly.io).
- **Semana 4:** README final, link no GitHub e primeiro post no LinkedIn
  mostrando o projeto rodando.

Plano completo em `claude/plano-4-semanas.md` no projeto Missão IA
Global.
