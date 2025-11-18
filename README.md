# Ngobrol.ai

Ngobrol.ai is a full-stack, production-ready AI dashboard and agent builder designed for custom LLM (Large Language Model) operations, analytics, and conversation management. It features a FastAPI backend with SQLAlchemy and a React (Vite + Tailwind) frontend.

---

## Features

- **Backend (FastAPI):**
  - Modular service for Agents, Analytics, Documents, API tools, Reports
  - Google SSO ready
  - RAG (Retrieval Augmented Generation) backend for document-augmented agents
  - PostgreSQL (default) or SQLite compatible
  - SQLAlchemy ORM with migrations scaffolded

- **Frontend (React/TypeScript/Tailwind):**
  - Agent CRUD and simulation dashboard
  - Conversation/session analytics and transcript viewing
  - API/Report request management

- **Pluggable:** Easily extend agents, docs, APIs, reporting, or integrate new LLMs.

---

## Repository Structure

```
ngobrolai/
│
├── app/                       # FastAPI backend
│   ├── main.py                # FastAPI app and routers include
│   ├── config.py              # Environment and secret/config management
│   ├── db.py                  # SQLAlchemy DB engine/setup
│   ├── dependencies/          # FastAPI dependency utilities
│   │   └── auth.py            # Auth helpers/dependencies
│   ├── models/                # SQLAlchemy ORM models
│   │   ├── user.py
│   │   ├── agent.py
│   │   ├── session.py
│   │   ├── message.py
│   │   ├── document.py
│   │   ├── api_tool.py
│   │   ├── api_test_log.py
│   │   ├── report_request.py
│   │   ├── document_vector.py
│   │   ├── agent_knowledge.py
│   │   ├── agent_api.py
│   │   └── __init__.py
│   ├── schemas/               # Pydantic models for API I/O
│   │   ├── user.py
│   │   ├── agent.py
│   │   ├── session.py
│   │   ├── document.py
│   │   ├── api_tool.py
│   │   └── report.py
│   ├── routers/               # API route groupings (REST endpoints)
│   │   ├── auth.py
│   │   ├── user.py
│   │   ├── agent.py
│   │   └── __init__.py
│   ├── services/              # (Optional) Services & logic beyond models
│   ├── utils/                 # Utility functions
│   ├── alembic/               # DB migrations (if using Alembic)
│   └── tests/                 # Backend unit/integration tests
│
├── frontend/
│   └── src/
│       ├── App.tsx
│       ├── main.tsx
│       ├── index.css
│       ├── pages/
│       │   ├── AgentManagementPage.tsx
│       │   └── ReportManagementPage.tsx
│       └── components/
│           ├── agents/
│           │   ├── AgentForm.tsx
│           │   ├── AgentListTable.tsx
│           │   └── AgentSimulator.tsx
│           └── reports/
│               ├── SessionHistoryTable.tsx
│               ├── ChatSessionDetail.tsx
│               ├── ReportRequestTable.tsx
│               └── ReportRequestForm.tsx
│
├── README.md                  # This file
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+
- (Recommended) PostgreSQL for production, SQLite for dev/testing

### Backend (FastAPI)

```bash
cd ngobrolai/app
python -m venv venv
source venv/bin/activate       # Or "venv\Scripts\activate" on Windows
pip install -r requirements.txt
# Setup .env or edit config.py for your DB
alembic upgrade head           # Run DB migrations if using Alembic
uvicorn main:app --reload
```

### Frontend (React)

```bash
cd ngobrolai/frontend
npm install
npm run dev
# Or "yarn" if using yarn
```

### API usage

- The backend API is served on `http://localhost:8000`
- Frontend can proxy or directly request `/agents/`, `/sessions/`, etc.
- Auth endpoints (`/auth/login`) can be configured for OAuth2/Google SSO.

---

## Customization

- **Add new agent types:** Extend models and add to `models/agent.py`, `schemas/agent.py`, and relevant routers.
- **Add API integrations:** Add models to `models/api_tool.py` and endpoint logic in routers/services.
- **Plug in new LLM or AI providers:** See `/services/llm/` and wire into your agent pipeline.

---

## License

MIT or as specified

---

## Community & Support

Questions/feature requests? 
Call Yosep
