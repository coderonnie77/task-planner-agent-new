"""
Streamlit Web UI for Task Planner Agent
Simple, beautiful interface for the agent
"""

import streamlit as st
import task_planner_agent as agent

# Page configuration
st.set_page_config(
    page_title="Task Planner Agent",
    page_icon="📋",
    layout="centered"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .step-box {
        background: #f0f2f6;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 4px solid #1f77b4;
    }
    .result-box {
        background: #e8f5e9;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 4px solid #4caf50;
    }
    .final-answer {
        background: #fff3e0;
        padding: 1.5rem;
        border-radius: 8px;
        margin-top: 1rem;
        border-left: 4px solid #ff9800;
        font-size: 1.1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-header">📋 Task Planner Agent</div>', unsafe_allow_html=True)

st.markdown("""
**Enter a task and the AI agent will:**
1. Break it into 3 steps
2. Execute each step one by one
3. Summarize into a final answer

*Built with LangGraph, LangChain & Ollama (llama3.2)*
""")

# Task Input
st.markdown("### 🎯 Enter Your Task")
user_task = st.text_area(
    "Task Description:",
    placeholder="e.g., Research the best laptops under ₹50,000 for students",
    height=100,
    max_chars=500
)

# Examples
st.markdown("### 💡 Try These Examples")
examples = [
    "Research the best laptops under ₹50,000",
    "Plan a 3-day trip to Goa",
    "Create a study plan for learning Python in 30 days",
    "Research the best hotels in Goa under $500"
]

col1, col2 = st.columns(2)
with col1:
    if st.button("📚 Example 1", use_container_width=True):
        user_task = examples[0]
with col2:
    if st.button("✈️ Example 2", use_container_width=True):
        user_task = examples[1]
with col1:
    if st.button("📚 Example 3", use_container_width=True):
        user_task = examples[2]
with col2:
    if st.button("🏨 Example 4", use_container_width=True):
        user_task = examples[3]

# Run Button
col1, col2 = st.columns([3, 1])
with col2:
    run_button = st.button("🚀 Start Planning", use_container_width=True)

# Run the agent
if run_button and user_task:
    with st.spinner("🤖 Agent is planning and executing..."):
        try:
            result = agent.run_task_planner(user_task)
            
            # Display Results
            st.success("✅ Task Completed!")
            
            # Steps
            st.markdown("### 📋 Planned Steps")
            for i, step in enumerate(result["steps"], 1):
                st.markdown(f'<div class="step-box"><strong>Step {i}:</strong> {step}</div>', unsafe_allow_html=True)
            
            # Results
            st.markdown("### 📊 Execution Results")
            for r in result["results"]:
                st.markdown(f'<div class="result-box">{r}</div>', unsafe_allow_html=True)
            
            # Final Answer
            st.markdown("### ✅ Final Answer")
            st.markdown(f'<div class="final-answer">{result["final_answer"]}</div>', unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

elif run_button and not user_task:
    st.warning("⚠️ Please enter a task first!")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666;">
    <p>🤖 Built with <strong>LangGraph</strong> | <strong>LangChain</strong> | <strong>Ollama</strong></p>
    <p>Beginner-friendly AI agent project for learning stateful workflows</p>
</div>
""", unsafe_allow_html=True)