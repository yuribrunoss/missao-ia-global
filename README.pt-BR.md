# 🌍 Missão IA Global

> AI Engineering roadmap, built one real project at a time — in public.

🇧🇷 Natal, Brazil • 🌎 Open to Remote Global Opportunities

🇺🇸 [English](README.md) · 🇧🇷 [Português](README.pt-BR.md) · 🇪🇸 [Español](README.es.md) · 🇫🇷 [Français](README.fr.md) · 🇮🇹 [Italiano](README.it.md)

---

## 🚀 O que é isso

**Missão IA Global** é o meu roadmap público de transição pra AI
Engineering / Backend Development. Em vez de acumular cursos, cada
volume só é marcado como concluído quando existe código real,
funcionando e testado de ponta a ponta.

Este repositório também guarda meu material de preparação de carreira
(currículo, LinkedIn, perfil do GitHub) e notas pessoais de engenharia —
mas o roadmap e o código entregue são a parte que importa pra quem for
avaliar o trabalho.

## 🧠 Projeto principal — Classificador de Feedbacks com IA

Uma API com IA que classifica feedbacks de clientes e decide por conta
própria quando um humano precisa entrar no processo.

- Classifica o sentimento (positivo / negativo / neutro) com justificativa, usando a **API do Gemini**.
- Sugere uma resposta pronta pra enviar.
- Um **agente de IA** (function calling, não uma regra fixa) decide se um caso precisa de atenção humana — e pode consultar casos parecidos antes de decidir.
- **PostgreSQL** em produção (migrado do SQLite pra que o histórico sobreviva a redeploys).
- **Containerizado** (API + Postgres via `docker-compose`).
- Publicado no **Render**, infraestrutura como código (`render.yaml`).

🔗 [Docs da API em produção](https://missao-ia-global-classificador.onrender.com/docs) · 📂 [`01-Python-IA/Projeto-Automacao-IA/`](01-Python-IA/Projeto-Automacao-IA/)

## 📚 Roadmap

| Volume | Foco | Status |
| --- | --- | --- |
| 1 — Python for AI | Primeira CLI com a API do Gemini | ✅ Concluído |
| 2 — Automação | Lógica de decisão + ação | ✅ Concluído |
| 3 — AI Agents | Function calling + memória | ✅ Concluído |
| 4 — Backend AI | PostgreSQL + Docker, em produção | ✅ Concluído |
| YUYU AI ERP | Future Hero Project — não iniciado | 🔜 Próximo |

Os quatro volumes concluídos são o mesmo projeto
(`01-Python-IA/Projeto-Automacao-IA/`), evoluído em camadas e validado
de ponta a ponta em cada etapa — veja o
[README do próprio projeto](01-Python-IA/Projeto-Automacao-IA/README.md)
pro detalhe técnico de cada volume.

## 🛠️ Stack Técnica

**Em uso:** Python · FastAPI · PostgreSQL · SQLite · Docker · API do Google Gemini (com function calling / agentes de IA) · Git & GitHub · VS Code · uv

**Próximo passo:** decidir o próximo projeto real — provavelmente a primeira fase do **YUYU AI ERP** (backend de ERP com FastAPI + PostgreSQL), que ainda não foi iniciado.

## 🗂️ Estrutura do Repositório

```text
MISSAO-IA-GLOBAL/
├── 00-Fundacao-IA/            # configuração de ambiente, primeiros exercícios
├── 01-Python-IA/              # o projeto real está aqui (Volumes 1-4)
├── 02-APIs-e-Automacoes/      # vazia de propósito — ver nota abaixo
├── 03-Agentes-IA/             # vazia de propósito — ver nota abaixo
├── 04-Backend-IA/             # vazia de propósito — ver nota abaixo
├── 05-Carreira-Internacional/ # currículo, LinkedIn, GitHub, preparação de carreira
├── 06-Metrics-OS/             # métricas pessoais de estudo/engenharia (planejado)
├── 07-Founder-OS/             # rotinas/planejamento pessoal (planejado)
├── 08-Project-Registry/       # registro de releases/marcos (planejado)
├── Assets/
├── Brand-System/              # identidade visual pessoal
├── Diario/                    # diário de engenharia
├── Engineering-Handbook/      # notas técnicas pessoais
├── Portfolio/
├── ROADMAP.md
├── PROJECT-MAP.md
├── CHANGELOG.md
└── README.md
```

**Nota:** `02-APIs-e-Automacoes/`, `03-Agentes-IA/` e `04-Backend-IA/`
continuam vazias de propósito. Os Volumes 2, 3 e 4 do roadmap foram
construídos *dentro* de `01-Python-IA/Projeto-Automacao-IA/` — o mesmo
projeto evoluído em camadas, sem recomeçar um módulo novo por volume.

## 🌎 Sobre mim

Sou um desenvolvedor brasileiro em transição pra AI Engineering, com
histórico em suporte de TI e operações digitais. Estou construindo esse
roadmap em público e me preparando pra oportunidades remotas (Brasil,
Europa, América do Norte).

- 💻 GitHub — [@yuribrunoss](https://github.com/yuribrunoss)
- 🔗 LinkedIn — Yuri Bruno

## 📜 Documentos relacionados

- [`ROADMAP.md`](ROADMAP.md) — o roadmap em mais detalhe.
- [`PROJECT-MAP.md`](PROJECT-MAP.md) — pra que serve cada pasta.
- [`CHANGELOG.md`](CHANGELOG.md) — histórico de versões.
- [`Diario/README.md`](Diario/README.md) — diário de engenharia.

> Construindo um projeto real por vez — documentado, testado e publicado em público.
