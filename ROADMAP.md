# 🛣️ Roadmap — Missão IA Global

A long-term plan for becoming an AI Engineer / Backend Developer through
real, shipped software — not just courses.

---

## 📦 Engineering Roadmap

| Volume | Focus | Status |
| --- | --- | --- |
| 1 — Python for AI | First Python + Gemini API project (CLI) | ✅ Concluded |
| 2 — Automation | Decision + action logic (no fixed rules) | ✅ Concluded |
| 3 — AI Agents | Function calling + memory/context | ✅ Concluded |
| 4 — Backend AI | PostgreSQL + Docker, deployed in production | ✅ Concluded |
| YUYU AI ERP | Future Hero Project | 🔜 Not started |

All four completed volumes are the same project —
`01-Python-IA/Projeto-Automacao-IA/` (the AI Feedback Classifier) — evolved
layer by layer. See its own README for the technical detail of each
volume.

---

## 📘 Volume 1 — Python for AI ✅

First real code in the roadmap: a CLI that sends customer feedback to the
Gemini API and classifies sentiment with a justification.

## 🤖 Volume 2 — Automation ✅

Added a suggested reply, and logic that flags negative feedback as
needing human follow-up (`ações pendentes`).

## 🧠 Volume 3 — AI Agents ✅

The fixed rule became a real decision: the Gemini model itself decides,
via function calling, whether a case needs follow-up — and can consult
similar past cases first (a short tool-use loop, capped at 4 steps so it
never runs unbounded).

## 🗄️ Volume 4 — Backend AI ✅

Migrated from SQLite to PostgreSQL so history survives redeploys,
containerized the app with Docker (API + Postgres via `docker-compose`),
and deployed with a managed Postgres database on Render via `render.yaml`
— validated end-to-end in production, including surviving a manual
redeploy.

## 🚀 Next — YUYU AI ERP (Future Hero Project)

Not started yet. Planned as a bigger, production-oriented ERP project
(FastAPI + PostgreSQL + AI features) once the next real project's scope
is decided. No fixed volume number until work actually begins.

---

## 🌎 Career Track (parallel — doesn't block the technical roadmap)

- English — daily practice, currently basic level.
- Career prep (résumé, LinkedIn, GitHub profile) — see `05-Carreira-Internacional/`.

---

## 📚 Related Documents

- `README.md`
- `PROJECT-MAP.md`
- `CHANGELOG.md`
- `Diario/README.md`

---

> One volume gets marked "Concluded" only after it's shipped, deployed and
> tested end-to-end — not when it's planned.
