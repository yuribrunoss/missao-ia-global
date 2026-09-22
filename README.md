# 🌍 Missão IA Global

> AI Engineering roadmap, built one real project at a time — in public.

🇧🇷 Natal, Brazil • 🌎 Open to Remote Global Opportunities

---

## 🚀 What this is

**Missão IA Global** is my public roadmap for transitioning into AI
Engineering / Backend Development. Instead of collecting courses, each
volume ships as real, running, end-to-end tested code before moving to the
next one.

This repo also holds my career-prep material (résumé, LinkedIn, GitHub
profile work) and personal engineering notes — but the roadmap and the
shipped code are the part that matters to anyone evaluating the work.

---

## 🧠 Flagship project — Classificador de Feedbacks com IA

An AI-powered API that classifies customer feedback and decides on its own
when a human needs to step in.

- Classifies sentiment (positive / negative / neutral) with a justification, via the **Gemini API**.
- Suggests a ready-to-send reply.
- An **AI agent** (function calling, not a fixed rule) decides whether a case needs human follow-up — and can check similar past cases before deciding.
- **PostgreSQL** in production (migrated from SQLite so history survives redeploys).
- **Dockerized** (API + Postgres via `docker-compose`).
- Deployed on **Render**, infrastructure as code (`render.yaml`).

🔗 [Live API docs](https://missao-ia-global-classificador.onrender.com/docs) · 📂 [`01-Python-IA/Projeto-Automacao-IA/`](01-Python-IA/Projeto-Automacao-IA/)

---

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

---

## 🛠️ Tech Stack

**In use:** Python · FastAPI · PostgreSQL · SQLite · Docker · Google Gemini API (incl. function calling / AI agents) · Git & GitHub · VS Code · uv

**Next up:** deciding the next real project — likely the first phase of **YUYU AI ERP** (FastAPI + PostgreSQL ERP backend), still not started.

---

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
layers, not restarted as a new module per volume. These folders will only
get real content when a future project is built as its own standalone
module.

---

## 🌎 About Me

I'm a Brazilian developer transitioning into AI Engineering, with a
background in IT support and digital operations. I'm building this
roadmap in public and preparing for remote opportunities (Brazil, Europe,
North America).

- 💻 GitHub — [@yuribrunoss](https://github.com/yuribrunoss)
- 🔗 LinkedIn — Yuri Bruno

---

## 📜 Related docs

- [`ROADMAP.md`](ROADMAP.md) — the roadmap in more detail.
- [`PROJECT-MAP.md`](PROJECT-MAP.md) — what each folder is for.
- [`CHANGELOG.md`](CHANGELOG.md) — version history.
- [`Diario/README.md`](Diario/README.md) — engineering journal.

---

> Building one real project at a time — documented, tested, and shipped in public.
