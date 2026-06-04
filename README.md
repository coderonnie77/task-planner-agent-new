# 🤖 Task Planner Agent - LangGraph Project

A beginner-friendly AI agent that breaks complex tasks into steps and executes them one by one using **LangGraph**.

## ✨ Features

- **Multi-step Planning**: AI breaks tasks into 3 logical steps
- **Sequential Execution**: Executes each step one by one
- **State Management**: Remembers progress and results
- **Looping**: Automatically loops until all steps complete
- **Summarization**: Combines results into clear final answer
- **Web UI**: Beautiful Streamlit interface
- **REST API**: FastAPI backend for integration
- **Docker Ready**: Easy deployment with Docker Compose

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **LangGraph** | Agent orchestration & stateful workflows |
| **LangChain** | LLM integration & tools |
| **OpenAI GPT-4o** | Core AI reasoning |
| **FastAPI** | REST API backend |
| **Streamlit** | Web UI frontend |
| **Docker** | Containerization |
| **Python 3.11** | Programming language |

## 📦 Installation & Setup

### Option 1: Local Development (Recommended for Learning)

```bash
# 1. Clone or create project folder
mkdir task-planner-agent
cd task-planner-agent

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# On Mac/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Create .env file
cp .env.example .env

# 6. Add your OpenAI API key to .env
# OPENAI_API_KEY=sk-your-key-here
```

### Option 2: Docker (Recommended for Production)

```bash
# 1. Create .env file with your API key
cp .env.example .env
# Edit .env and add your OpenAI API key

# 2. Build and run with Docker Compose
docker-compose up --build
```

## 🚀 Running the Project

### Local Development

```bash
# Terminal 1: Run FastAPI backend
uvicorn app:app --reload --host 0.0.0.0 --port 8000

# Terminal 2: Run Streamlit UI (in another terminal)
streamlit run app_ui.py --server.address=0.0.0.0 --server.port=8501
```

### Docker

```bash
# Start all services
docker-compose up --build

# Stop services
docker-compose down
```

## 🌐 Access the Application

| Service | URL | Description |
|---------|-----|-------------|
| **FastAPI Docs** | http://localhost:8000/docs | Swagger API documentation |
| **Streamlit UI** | http://localhost:8501 | Web interface |
| **Health Check** | http://localhost:8000/health | API health status |

## 🧪 Testing

### Test via CLI (Built-in)

```bash
python task_planner_agent.py
```

### Test via API

```bash
# Using curl
curl -X POST http://localhost:8000/api/v1/planner \
  -H "Content-Type: application/json" \
  -d '{"task": "Research the best laptops under ₹50,000"}'

# Using Python
import requests
response = requests.post("http://localhost:8000/api/v1/planner", json={
    "task": "Research the best laptops under ₹50,000"
})
print(response.json())
```

## 📁 Project Structure
