# 🌍 Missão IA Global

> AI Engineering roadmap, built one real project at a time — in public.

🇧🇷 Natal, Brazil • 🌎 Open to Remote Global Opportunities

🇺🇸 [English](README.md) · 🇧🇷 [Português](README.pt-BR.md) · 🇪🇸 [Español](README.es.md) · 🇫🇷 [Français](README.fr.md) · 🇮🇹 [Italiano](README.it.md)

---

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
