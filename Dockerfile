FROM python:3.11-slim

WORKDIR /app

# Install system dependencies including zstd for Ollama
RUN apt-get update && apt-get install -y \
    curl \
    zstd \
    && rm -rf /var/lib/apt/lists/*

# Install Ollama
RUN curl -fsSL https://ollama.ai/install.sh | sh

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port (Render requires $PORT environment variable)
ENV PORT=8080
ENV STREAMLIT_SERVER_PORT=8080
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0
ENV STREAMLIT_SERVER_HEADLESS=1

# Run Streamlit
CMD ["streamlit", "run", "app_ui.py", "--server.address=0.0.0.0", "--server.port=8080"]