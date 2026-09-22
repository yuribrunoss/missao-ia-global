# 🌍 Missão IA Global

> AI Engineering roadmap, built one real project at a time — in public.

🇧🇷 Natal, Brazil • 🌎 Open to Remote Global Opportunities

🇺🇸 [English](README.md) · 🇧🇷 [Português](README.pt-BR.md) · 🇪🇸 [Español](README.es.md) · 🇫🇷 [Français](README.fr.md) · 🇮🇹 [Italiano](README.it.md)

---

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
