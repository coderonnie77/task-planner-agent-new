from typing import TypedDict, List
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import HumanMessage
import ast
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class TaskState(TypedDict):
    task: str
    steps: List[str]
    current_step: int
    results: List[str]
    final_answer: str

# Use Ollama with llama3.2 (runs locally, free, no API key)
llm = ChatOllama(model="llama3.2", temperature=0)

def plan_steps(state: TaskState) -> TaskState:
    prompt = f"""
    Break down this task into 3 simple steps:
    Task: {state['task']}
    
    Return ONLY a Python list of 3 steps like this:
    ["step 1", "step 2", "step 3"]
    Do not add any other text.
    """
    
    response = llm.invoke([HumanMessage(content=prompt)])
    steps_text = response.content.replace("```python", "").replace("```", "").strip()
    
    try:
        steps = ast.literal_eval(steps_text)
        if not isinstance(steps, list) or len(steps) != 3:
            steps = ["Step 1: Start", "Step 2: Process", "Step 3: Complete"]
    except:
        steps = ["Step 1: Start", "Step 2: Process", "Step 3: Complete"]
    
    return {"task": state["task"], "steps": steps, "current_step": 0, "results": [], "final_answer": ""}

def execute_step(state: TaskState) -> TaskState:
    step_num = state["current_step"]
    step = state["steps"][step_num]
    
    prompt = f"""
    Execute this step and provide the result:
    Step {step_num + 1}: {step}
    Task: {state['task']}
    
    Return a short result (1-2 sentences).
    """
    
    response = llm.invoke([HumanMessage(content=prompt)])
    result = response.content.strip()
    
    results = state["results"].copy() if isinstance(state["results"], list) else []
    results.append(f"Step {step_num + 1}: {result}")
    
    return {"task": state["task"], "steps": state["steps"], "current_step": step_num + 1, "results": results, "final_answer": state["final_answer"]}

def check_progress(state: TaskState) -> str:
    if state["current_step"] >= len(state["steps"]):
        return "finish"
    return "continue"

def summarize_results(state: TaskState) -> TaskState:
    results_text = "\n".join(state["results"])
    prompt = f"Summarize results into final answer:\n\nResults:\n{results_text}\n\nTask: {state['task']}"
    
    response = llm.invoke([HumanMessage(content=prompt)])
    return {**state, "final_answer": response.content.strip()}

workflow = StateGraph(TaskState)
workflow.add_node("plan", plan_steps)
workflow.add_node("execute", execute_step)
workflow.add_node("summarize", summarize_results)
workflow.add_edge(START, "plan")
workflow.add_edge("plan", "execute")
workflow.add_conditional_edges("execute", check_progress, {"continue": "execute", "finish": "summarize"})
workflow.add_edge("summarize", END)

agent = workflow.compile()

def run_task_planner(task: str) -> dict:
    result = agent.invoke({"task": task})
    return {"task": result["task"], "steps": result["steps"], "results": result["results"], "final_answer": result["final_answer"]}

if __name__ == "__main__":
    print("="*70)
    print("🤖 Task Planner Agent - LangGraph Demo")
    print("="*70)
    
    task = input("\nEnter your task: ")
    
    print(f"\n📋 Planning: {task}\n")
    print("🔄 Agent is working (this may take 10-20 seconds)...\n")
    result = run_task_planner(task)
    
    print("\n📋 Steps:")
    for i, step in enumerate(result["steps"], 1):
        print(f"  {i}. {step}")
    
    print("\n📊 Results:")
    for r in result["results"]:
        print(f"  • {r}")
    
    print(f"\n✅ Final Answer:\n{result['final_answer']}")
    print("="*70)