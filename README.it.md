# 🌍 Missão IA Global

> AI Engineering roadmap, built one real project at a time — in public.

🇧🇷 Natal, Brazil • 🌎 Open to Remote Global Opportunities

🇺🇸 [English](README.md) · 🇧🇷 [Português](README.pt-BR.md) · 🇪🇸 [Español](README.es.md) · 🇫🇷 [Français](README.fr.md) · 🇮🇹 [Italiano](README.it.md)

---

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
