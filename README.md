# 🤖 BuildBuddy

### AI Coding Companion with Persistent Project Memory

BuildBuddy is an AI coding companion that remembers important project information such as coding decisions, bugs, solutions, technologies, and developer preferences.

Instead of treating every conversation as a fresh start, BuildBuddy uses **Hindsight memory** to retain and recall project context.

---

## 🧠 What Makes BuildBuddy Different?

Normal coding assistants can forget important project decisions between conversations.

BuildBuddy solves this by giving the assistant **persistent project memory**.

For example, a developer can tell BuildBuddy:

> Use JWT authentication with 30-minute access tokens and PostgreSQL.

Later, the developer can ask:

> How should I implement authentication?

BuildBuddy can recall the previous decision and provide an answer based on the project's stored context.

---

## ✨ Features

- 🧠 Persistent project memory using Hindsight
- 💬 AI-powered coding conversation
- 🔍 Semantic memory search
- 🐛 Remembers bugs and their solutions
- ⚙️ Remembers project architecture decisions
- 👨‍💻 Remembers developer coding preferences
- 🧩 FastAPI backend
- 🐘 PostgreSQL project architecture
- 🔐 JWT authentication architecture
- 📊 Project memory counter
- 🧠 Shows when project memory is used

---

## 🛠️ Tech Stack

- Python
- FastAPI
- Hindsight
- PostgreSQL
- JWT Authentication
- HTML
- CSS
- JavaScript

---

## 🔄 How It Works

```text
Developer
    │
    ▼
Ask BuildBuddy
    │
    ▼
Hindsight Memory
    │
    ▼
Recall Project Context
    │
    ▼
BuildBuddy AI
    │
    ▼
Answer
    │
    ▼
Store New Memory