# Projeto de Automação com IA

Projeto prático da Missão IA Global: automação com IA que evolui semana a
semana.

## Estrutura

- `nucleo.py` — toda a lógica de verdade: chamar a IA, interpretar a
  resposta, guardar/ler o histórico no SQLite. Nem o CLI nem a API
  duplicam essa lógica, os dois só importam daqui.
- `classificador.py` — a versão de terminal (CLI).
- `api.py` — a mesma lógica exposta como API HTTP, com FastAPI.
- `historico.db` — banco SQLite local (não vai pro git, é dado seu).

## O que ele faz hoje

Recebe um feedback de cliente (texto livre) e usa a API do Gemini pra:

1. **Classificar** o sentimento — positivo, negativo ou neutro — com
   justificativa.
2. **Sugerir uma resposta** pronta pra enviar ao cliente, coerente com
   o sentimento identificado.
3. **Decidir e agir**: um agente (via function calling do Gemini) decide
   se o caso precisa de uma "ação pendente" — não é mais uma regra fixa
   tipo "se for negativo, sempre cria"; o próprio modelo avalia o caso e
   escreve o motivo quando decide agir.
4. **Consultar o histórico antes de decidir**: o agente pode, por conta
   própria, checar se já apareceram casos parecidos antes e usar isso
   pra reforçar a decisão — por exemplo, apontando que é um problema
   recorrente.

Tudo isso fica salvo num histórico local. Duas formas de usar:

### 1. Pelo terminal (CLI)

```bash
uv run classificador.py
```

Digite um feedback, veja a classificação e a resposta sugerida. Digite
`historico` pra ver o que já foi salvo, `acoes` pra ver as ações
pendentes (feedbacks negativos que precisam de atenção), e `sair` para
encerrar.

### 2. Pela API (FastAPI)

```bash
uv run uvicorn api:app --reload
```

Depois abra http://127.0.0.1:8000/docs no navegador — o FastAPI gera
uma página interativa sozinho, onde dá pra testar os endpoints sem
escrever nenhum código:

- `POST /classificar` — manda `{"feedback": "seu texto aqui"}`, recebe
  de volta o sentimento, a justificativa, a resposta sugerida, se uma
  ação pendente foi criada (`acao_pendente_criada`) e o motivo escrito
  pelo próprio agente quando ele decide agir (`motivo_acao_pendente`).
- `GET /historico?limite=5` — devolve as últimas classificações salvas.
- `GET /acoes-pendentes?limite=20` — devolve os feedbacks negativos que
  ainda precisam de atenção humana.

Problema de negócio que representa: qualquer sistema (um site, um
chatbot, uma planilha automatizada) pode chamar essa API pra classificar
feedbacks em tempo real, já sair com uma resposta pronta pra usar, e
saber automaticamente quais casos precisam de atenção — sem precisar de
alguém digitando no terminal ou lendo feedback por feedback.

## Como configurar (primeira vez, local)

1. Tenha o [uv](https://docs.astral.sh/uv/) instalado.
2. Copie `.env.example` para `.env` e cole sua chave grátis da API do
   Gemini (pegue em https://aistudio.google.com/apikey).
3. Instale as dependências:
   ```bash
   uv sync
   ```

## Deploy público (Render)

A API roda de graça no [Render](https://render.com), usando o Blueprint
`render.yaml` que está na raiz do repositório (`MISSAO-IA-GLOBAL/render.yaml`).
Passo a passo em `claude/plano-4-semanas.md` no projeto Missão IA Global,
resumo:

1. Criar conta no Render e conectar o repositório `MISSAO-IA-GLOBAL`.
2. Criar um "Blueprint" a partir do `render.yaml` — ele já configura o
   build (`uv sync`) e o start (`uvicorn`) sozinho.
3. Definir a variável de ambiente `GOOGLE_API_KEY` no painel do Render
   (nunca vai pro git — o Blueprint só reserva o nome).
4. Aguardar o primeiro deploy e testar em `https://<nome-do-serviço>.onrender.com/docs`.

**Limitações do plano grátis (esperadas, não são bugs):**
- O serviço "dorme" depois de 15 min sem receber requisição, e a
  primeira chamada depois disso demora ~1 min pra responder (ele está
  "ligando" de novo).
- O disco é temporário: a cada novo deploy ou "sono" prolongado, o
  `historico.db` reseta e recomeça vazio. Serve bem para demonstrar que
  a API funciona; se quiser histórico permanente, o próximo passo seria
  trocar o SQLite local por um banco Postgres gerenciado (fora do
  escopo das 4 semanas).

## Próximas etapas (plano)

Esse projeto é a base do **Volume 1 — Python for AI**, do **Volume 2 —
Automação com IA (decisão + ação)** e agora também do **Volume 3 — AI
Agents** (decisão via function calling + memória/contexto) do roadmap
da Missão IA Global. Depois do Volume 3, o próximo passo é backend de
verdade (Volume 4 — PostgreSQL + Docker).

Planos completos no projeto Missão IA Global:
- `claude/plano-4-semanas.md` — Volume 1 (concluído).
- `claude/plano-volume-2.md` — Volume 2 (concluído).
- `claude/plano-volume-3.md` — Volume 3 (em andamento — Semanas 1 e 2 concluídas).
