# 🌍 Missão IA Global

> AI Engineering roadmap, built one real project at a time — in public.

🇧🇷 Natal, Brazil • 🌎 Open to Remote Global Opportunities

🇺🇸 [English](#lang-en) · 🇧🇷 [Português](#lang-pt) · 🇪🇸 [Español](#lang-es) · 🇫🇷 [Français](#lang-fr) · 🇮🇹 [Italiano](#lang-it)

---

<details open>
<summary><strong>🇺🇸 English</strong></summary>
<a id="lang-en"></a>

## 🚀 What this is

**Missão IA Global** is my public roadmap for transitioning into AI
Engineering / Backend Development. Instead of collecting courses, each
volume ships as real, running, end-to-end tested code before moving to the
next one.

This repo also holds my career-prep material (résumé, LinkedIn, GitHub
profile work) and personal engineering notes — but the roadmap and the
shipped code are the part that matters to anyone evaluating the work.

## 🧠 Flagship project — AI Feedback Classifier

An AI-powered API that classifies customer feedback and decides on its own
when a human needs to step in.

- Classifies sentiment (positive / negative / neutral) with a justification, via the **Gemini API**.
- Suggests a ready-to-send reply.
- An **AI agent** (function calling, not a fixed rule) decides whether a case needs human follow-up — and can check similar past cases before deciding.
- **PostgreSQL** in production (migrated from SQLite so history survives redeploys).
- **Dockerized** (API + Postgres via `docker-compose`).
- Deployed on **Render**, infrastructure as code (`render.yaml`).

🔗 [Live API docs](https://missao-ia-global-classificador.onrender.com/docs) · 📂 [`01-Python-IA/Projeto-Automacao-IA/`](01-Python-IA/Projeto-Automacao-IA/)

## 📚 Roadmap

| Volume | Focus | Status |
| --- | --- | --- |
| 1 — Python for AI | First Gemini-powered CLI | ✅ Concluded |
| 2 — Automation | Decision + action logic | ✅ Concluded |
| 3 — AI Agents | Function calling + memory | ✅ Concluded |
| 4 — Backend AI | PostgreSQL + Docker, in production | ✅ Concluded |
| YUYU AI ERP | Future Hero Project — not started | 🔜 Next |

All four completed volumes are the same project
(`01-Python-IA/Projeto-Automacao-IA/`), evolved in layers and validated
end-to-end at each step — see the
[project's own README](01-Python-IA/Projeto-Automacao-IA/README.md) for
the technical detail of each volume.

## 🛠️ Tech Stack

**In use:** Python · FastAPI · PostgreSQL · SQLite · Docker · Google Gemini API (incl. function calling / AI agents) · Git & GitHub · VS Code · uv

**Next up:** deciding the next real project — likely the first phase of **YUYU AI ERP** (FastAPI + PostgreSQL ERP backend), still not started.

## 🗂️ Repository Structure

```text
MISSAO-IA-GLOBAL/
├── 00-Fundacao-IA/            # environment setup, first exercises
├── 01-Python-IA/              # the real project lives here (Volumes 1-4)
├── 02-APIs-e-Automacoes/      # empty on purpose — see note below
├── 03-Agentes-IA/             # empty on purpose — see note below
├── 04-Backend-IA/             # empty on purpose — see note below
├── 05-Carreira-Internacional/ # résumé, LinkedIn, GitHub, career prep
├── 06-Metrics-OS/             # personal study/engineering metrics (planned)
├── 07-Founder-OS/             # personal routines/planning (planned)
├── 08-Project-Registry/       # release/milestone log (planned)
├── Assets/
├── Brand-System/              # personal visual identity
├── Diario/                    # engineering journal
├── Engineering-Handbook/      # personal technical notes
├── Portfolio/
├── ROADMAP.md
├── PROJECT-MAP.md
├── CHANGELOG.md
└── README.md
```

**Note:** `02-APIs-e-Automacoes/`, `03-Agentes-IA/` and `04-Backend-IA/`
are still empty on purpose. Volumes 2, 3 and 4 of the roadmap were built
*inside* `01-Python-IA/Projeto-Automacao-IA/` — the same project evolved in
layers, not restarted as a new module per volume.

## 🌎 About Me

I'm a Brazilian developer transitioning into AI Engineering, with a
background in IT support and digital operations. I'm building this
roadmap in public and preparing for remote opportunities (Brazil, Europe,
North America).

- 💻 GitHub — [@yuribrunoss](https://github.com/yuribrunoss)
- 🔗 LinkedIn — Yuri Bruno

## 📜 Related docs

- [`ROADMAP.md`](ROADMAP.md) — the roadmap in more detail.
- [`PROJECT-MAP.md`](PROJECT-MAP.md) — what each folder is for.
- [`CHANGELOG.md`](CHANGELOG.md) — version history.
- [`Diario/README.md`](Diario/README.md) — engineering journal.

> Building one real project at a time — documented, tested, and shipped in public.

</details>

<details>
<summary><strong>🇧🇷 Português</strong></summary>
<a id="lang-pt"></a>

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

</details>

<details>
<summary><strong>🇪🇸 Español</strong></summary>
<a id="lang-es"></a>

## 🚀 Qué es esto

**Missão IA Global** es mi roadmap público de transición hacia AI
Engineering / Backend Development. En lugar de acumular cursos, cada
volumen se marca como terminado solo cuando hay código real, funcionando
y probado de punta a punta.

Este repositorio también guarda mi material de preparación profesional
(currículum, LinkedIn, perfil de GitHub) y notas personales de
ingeniería — pero el roadmap y el código entregado son lo que importa
para quien evalúe el trabajo.

## 🧠 Proyecto principal — Clasificador de Feedback con IA

Una API con IA que clasifica el feedback de clientes y decide por sí
misma cuándo un humano necesita intervenir.

- Clasifica el sentimiento (positivo / negativo / neutro) con justificación, usando la **API de Gemini**.
- Sugiere una respuesta lista para enviar.
- Un **agente de IA** (function calling, no una regla fija) decide si un caso necesita seguimiento humano — y puede consultar casos similares antes de decidir.
- **PostgreSQL** en producción (migrado desde SQLite para que el historial sobreviva a los redeploys).
- **Dockerizado** (API + Postgres vía `docker-compose`).
- Desplegado en **Render**, infraestructura como código (`render.yaml`).

🔗 [Documentación de la API en vivo](https://missao-ia-global-classificador.onrender.com/docs) · 📂 [`01-Python-IA/Projeto-Automacao-IA/`](01-Python-IA/Projeto-Automacao-IA/)

## 📚 Roadmap

| Volumen | Enfoque | Estado |
| --- | --- | --- |
| 1 — Python for AI | Primer CLI con la API de Gemini | ✅ Concluido |
| 2 — Automatización | Lógica de decisión + acción | ✅ Concluido |
| 3 — AI Agents | Function calling + memoria | ✅ Concluido |
| 4 — Backend AI | PostgreSQL + Docker, en producción | ✅ Concluido |
| YUYU AI ERP | Future Hero Project — no iniciado | 🔜 Siguiente |

Los cuatro volúmenes concluidos son el mismo proyecto
(`01-Python-IA/Projeto-Automacao-IA/`), evolucionado en capas y validado
de punta a punta en cada etapa — ver el
[README del propio proyecto](01-Python-IA/Projeto-Automacao-IA/README.md)
para el detalle técnico de cada volumen.

## 🛠️ Stack Tecnológico

**En uso:** Python · FastAPI · PostgreSQL · SQLite · Docker · API de Google Gemini (incl. function calling / agentes de IA) · Git & GitHub · VS Code · uv

**Próximo paso:** decidir el próximo proyecto real — probablemente la primera fase de **YUYU AI ERP** (backend de ERP con FastAPI + PostgreSQL), todavía no iniciado.

## 🗂️ Estructura del Repositorio

```text
MISSAO-IA-GLOBAL/
├── 00-Fundacao-IA/            # configuración del entorno, primeros ejercicios
├── 01-Python-IA/              # el proyecto real está aquí (Volúmenes 1-4)
├── 02-APIs-e-Automacoes/      # vacía a propósito — ver nota abajo
├── 03-Agentes-IA/             # vacía a propósito — ver nota abajo
├── 04-Backend-IA/             # vacía a propósito — ver nota abajo
├── 05-Carreira-Internacional/ # currículum, LinkedIn, GitHub, preparación profesional
├── 06-Metrics-OS/             # métricas personales de estudio/ingeniería (planeado)
├── 07-Founder-OS/             # rutinas/planificación personal (planeado)
├── 08-Project-Registry/       # registro de releases/hitos (planeado)
├── Assets/
├── Brand-System/              # identidad visual personal
├── Diario/                    # diario de ingeniería
├── Engineering-Handbook/      # notas técnicas personales
├── Portfolio/
├── ROADMAP.md
├── PROJECT-MAP.md
├── CHANGELOG.md
└── README.md
```

**Nota:** `02-APIs-e-Automacoes/`, `03-Agentes-IA/` y `04-Backend-IA/`
siguen vacías a propósito. Los Volúmenes 2, 3 y 4 del roadmap se
construyeron *dentro* de `01-Python-IA/Projeto-Automacao-IA/` — el mismo
proyecto evolucionado en capas, sin reiniciar un módulo nuevo por
volumen.

## 🌎 Sobre mí

Soy un desarrollador brasileño en transición hacia AI Engineering, con
experiencia en soporte de TI y operaciones digitales. Estoy construyendo
este roadmap en público y preparándome para oportunidades remotas
(Brasil, Europa, Norteamérica).

- 💻 GitHub — [@yuribrunoss](https://github.com/yuribrunoss)
- 🔗 LinkedIn — Yuri Bruno

## 📜 Documentos relacionados

- [`ROADMAP.md`](ROADMAP.md) — el roadmap con más detalle.
- [`PROJECT-MAP.md`](PROJECT-MAP.md) — para qué sirve cada carpeta.
- [`CHANGELOG.md`](CHANGELOG.md) — historial de versiones.
- [`Diario/README.md`](Diario/README.md) — diario de ingeniería.

> Construyendo un proyecto real a la vez — documentado, probado y publicado en público.

</details>

<details>
<summary><strong>🇫🇷 Français</strong></summary>
<a id="lang-fr"></a>

## 🚀 De quoi s'agit-il

**Missão IA Global** est ma feuille de route publique pour ma
reconversion vers l'AI Engineering / le développement backend. Plutôt
que d'accumuler des cours, chaque volume n'est marqué comme terminé que
lorsqu'il existe du code réel, fonctionnel et testé de bout en bout.

Ce dépôt contient aussi mon matériel de préparation de carrière (CV,
LinkedIn, profil GitHub) et mes notes d'ingénierie personnelles — mais
la feuille de route et le code livré sont ce qui compte pour quiconque
évalue ce travail.

## 🧠 Projet phare — Classificateur de retours clients par IA

Une API basée sur l'IA qui classe les retours clients et décide
elle-même quand une intervention humaine est nécessaire.

- Classe le sentiment (positif / négatif / neutre) avec justification, via l'**API Gemini**.
- Suggère une réponse prête à envoyer.
- Un **agent IA** (function calling, pas une règle fixe) décide si un cas nécessite un suivi humain — et peut consulter des cas similaires avant de décider.
- **PostgreSQL** en production (migré depuis SQLite pour que l'historique survive aux redéploiements).
- **Conteneurisé** (API + Postgres via `docker-compose`).
- Déployé sur **Render**, infrastructure as code (`render.yaml`).

🔗 [Documentation de l'API en ligne](https://missao-ia-global-classificador.onrender.com/docs) · 📂 [`01-Python-IA/Projeto-Automacao-IA/`](01-Python-IA/Projeto-Automacao-IA/)

## 📚 Feuille de route

| Volume | Objectif | Statut |
| --- | --- | --- |
| 1 — Python for AI | Premier CLI propulsé par Gemini | ✅ Terminé |
| 2 — Automatisation | Logique de décision + action | ✅ Terminé |
| 3 — AI Agents | Function calling + mémoire | ✅ Terminé |
| 4 — Backend AI | PostgreSQL + Docker, en production | ✅ Terminé |
| YUYU AI ERP | Future Hero Project — pas encore commencé | 🔜 Prochain |

Les quatre volumes terminés forment le même projet
(`01-Python-IA/Projeto-Automacao-IA/`), qui a évolué par couches et a
été validé de bout en bout à chaque étape — voir le
[README du projet lui-même](01-Python-IA/Projeto-Automacao-IA/README.md)
pour le détail technique de chaque volume.

## 🛠️ Stack Technique

**Utilisé :** Python · FastAPI · PostgreSQL · SQLite · Docker · API Google Gemini (incl. function calling / agents IA) · Git & GitHub · VS Code · uv

**Prochaine étape :** décider du prochain projet réel — probablement la première phase de **YUYU AI ERP** (backend ERP en FastAPI + PostgreSQL), pas encore commencé.

## 🗂️ Structure du dépôt

```text
MISSAO-IA-GLOBAL/
├── 00-Fundacao-IA/            # configuration de l'environnement, premiers exercices
├── 01-Python-IA/              # le projet réel se trouve ici (Volumes 1-4)
├── 02-APIs-e-Automacoes/      # vide intentionnellement — voir note ci-dessous
├── 03-Agentes-IA/             # vide intentionnellement — voir note ci-dessous
├── 04-Backend-IA/             # vide intentionnellement — voir note ci-dessous
├── 05-Carreira-Internacional/ # CV, LinkedIn, GitHub, préparation de carrière
├── 06-Metrics-OS/             # métriques personnelles d'étude/ingénierie (prévu)
├── 07-Founder-OS/             # routines/planification personnelles (prévu)
├── 08-Project-Registry/       # journal des releases/jalons (prévu)
├── Assets/
├── Brand-System/              # identité visuelle personnelle
├── Diario/                    # journal d'ingénierie
├── Engineering-Handbook/      # notes techniques personnelles
├── Portfolio/
├── ROADMAP.md
├── PROJECT-MAP.md
├── CHANGELOG.md
└── README.md
```

**Note :** `02-APIs-e-Automacoes/`, `03-Agentes-IA/` et `04-Backend-IA/`
sont encore vides intentionnellement. Les Volumes 2, 3 et 4 de la feuille
de route ont été construits *à l'intérieur* de
`01-Python-IA/Projeto-Automacao-IA/` — le même projet qui a évolué par
couches, sans redémarrer un nouveau module par volume.

## 🌎 À propos de moi

Je suis un développeur brésilien en reconversion vers l'AI Engineering,
avec une expérience en support IT et opérations numériques. Je construis
cette feuille de route en public et je me prépare pour des opportunités
à distance (Brésil, Europe, Amérique du Nord).

- 💻 GitHub — [@yuribrunoss](https://github.com/yuribrunoss)
- 🔗 LinkedIn — Yuri Bruno

## 📜 Documents liés

- [`ROADMAP.md`](ROADMAP.md) — la feuille de route en détail.
- [`PROJECT-MAP.md`](PROJECT-MAP.md) — à quoi sert chaque dossier.
- [`CHANGELOG.md`](CHANGELOG.md) — historique des versions.
- [`Diario/README.md`](Diario/README.md) — journal d'ingénierie.

> Construire un projet réel à la fois — documenté, testé et publié en public.

</details>

<details>
<summary><strong>🇮🇹 Italiano</strong></summary>
<a id="lang-it"></a>

## 🚀 Di cosa si tratta

**Missão IA Global** è la mia roadmap pubblica per la transizione verso
l'AI Engineering / lo sviluppo backend. Invece di accumulare corsi, ogni
volume viene segnato come concluso solo quando esiste codice reale,
funzionante e testato end-to-end.

Questo repository contiene anche il mio materiale di preparazione
professionale (CV, LinkedIn, profilo GitHub) e note personali di
ingegneria — ma la roadmap e il codice consegnato sono la parte che
conta per chi valuta il lavoro.

## 🧠 Progetto di punta — Classificatore di feedback con IA

Un'API basata su IA che classifica il feedback dei clienti e decide da
sola quando serve l'intervento di una persona.

- Classifica il sentimento (positivo / negativo / neutro) con giustificazione, tramite l'**API Gemini**.
- Suggerisce una risposta pronta da inviare.
- Un **agente IA** (function calling, non una regola fissa) decide se un caso necessita di un follow-up umano — e può consultare casi simili prima di decidere.
- **PostgreSQL** in produzione (migrato da SQLite affinché la cronologia sopravviva ai redeploy).
- **Containerizzato** (API + Postgres via `docker-compose`).
- Distribuito su **Render**, infrastruttura come codice (`render.yaml`).

🔗 [Documentazione API live](https://missao-ia-global-classificador.onrender.com/docs) · 📂 [`01-Python-IA/Projeto-Automacao-IA/`](01-Python-IA/Projeto-Automacao-IA/)

## 📚 Roadmap

| Volume | Focus | Stato |
| --- | --- | --- |
| 1 — Python for AI | Primo CLI basato su Gemini | ✅ Concluso |
| 2 — Automazione | Logica di decisione + azione | ✅ Concluso |
| 3 — AI Agents | Function calling + memoria | ✅ Concluso |
| 4 — Backend AI | PostgreSQL + Docker, in produzione | ✅ Concluso |
| YUYU AI ERP | Future Hero Project — non iniziato | 🔜 Prossimo |

I quattro volumi conclusi sono lo stesso progetto
(`01-Python-IA/Projeto-Automacao-IA/`), evoluto a strati e validato
end-to-end a ogni passaggio — vedi il
[README del progetto stesso](01-Python-IA/Projeto-Automacao-IA/README.md)
per il dettaglio tecnico di ogni volume.

## 🛠️ Stack Tecnologico

**In uso:** Python · FastAPI · PostgreSQL · SQLite · Docker · API Google Gemini (incl. function calling / agenti IA) · Git & GitHub · VS Code · uv

**Prossimo passo:** decidere il prossimo progetto reale — probabilmente la prima fase di **YUYU AI ERP** (backend ERP con FastAPI + PostgreSQL), non ancora iniziato.

## 🗂️ Struttura del Repository

```text
MISSAO-IA-GLOBAL/
├── 00-Fundacao-IA/            # configurazione dell'ambiente, primi esercizi
├── 01-Python-IA/              # il progetto reale si trova qui (Volumi 1-4)
├── 02-APIs-e-Automacoes/      # vuota di proposito — vedi nota sotto
├── 03-Agentes-IA/             # vuota di proposito — vedi nota sotto
├── 04-Backend-IA/             # vuota di proposito — vedi nota sotto
├── 05-Carreira-Internacional/ # CV, LinkedIn, GitHub, preparazione professionale
├── 06-Metrics-OS/             # metriche personali di studio/ingegneria (pianificato)
├── 07-Founder-OS/             # routine/pianificazione personale (pianificato)
├── 08-Project-Registry/       # registro di release/traguardi (pianificato)
├── Assets/
├── Brand-System/              # identità visiva personale
├── Diario/                    # diario di ingegneria
├── Engineering-Handbook/      # note tecniche personali
├── Portfolio/
├── ROADMAP.md
├── PROJECT-MAP.md
├── CHANGELOG.md
└── README.md
```

**Nota:** `02-APIs-e-Automacoes/`, `03-Agentes-IA/` e `04-Backend-IA/`
restano vuote di proposito. I Volumi 2, 3 e 4 della roadmap sono stati
costruiti *dentro* `01-Python-IA/Projeto-Automacao-IA/` — lo stesso
progetto evoluto a strati, senza ripartire con un nuovo modulo per ogni
volume.

## 🌎 Chi sono

Sono uno sviluppatore brasiliano in transizione verso l'AI Engineering,
con un background in supporto IT e operazioni digitali. Sto costruendo
questa roadmap in pubblico e mi sto preparando per opportunità da remoto
(Brasile, Europa, Nord America).

- 💻 GitHub — [@yuribrunoss](https://github.com/yuribrunoss)
- 🔗 LinkedIn — Yuri Bruno

## 📜 Documenti correlati

- [`ROADMAP.md`](ROADMAP.md) — la roadmap più in dettaglio.
- [`PROJECT-MAP.md`](PROJECT-MAP.md) — a cosa serve ogni cartella.
- [`CHANGELOG.md`](CHANGELOG.md) — cronologia delle versioni.
- [`Diario/README.md`](Diario/README.md) — diario di ingegneria.

> Costruire un progetto reale alla volta — documentato, testato e pubblicato in pubblico.

</details>
