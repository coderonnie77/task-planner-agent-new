from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import task_planner_agent as agent

app = FastAPI(
    title="Task Planner Agent API",
    description="API for LangGraph Task Planner Agent",
    version="1.0.0"
)

class TaskRequest(BaseModel):
    task: str

class TaskResponse(BaseModel):
    task: str
    steps: List[str]
    results: List[str]
    final_answer: str

@app.get("/")
def root():
    return {
        "message": "🤖 Task Planner Agent API",
        "docs": "/docs"
    }

@app.get("/health")
def health():
    return {"status": "ok", "agent": "Task Planner Agent"}

@app.post("/api/v1/planner", response_model=TaskResponse)
def planner(request: TaskRequest):
    """
    Execute a task and return the result.
    
    **Example:**
    ```json
    {
        "task": "Research the best laptops under ₹50,000"
    }
    ```
    """
    result = agent.run_task_planner(request.task)
    return result

# Run with: uvicorn app:app --reload --host 0.0.0.0 --port 8000