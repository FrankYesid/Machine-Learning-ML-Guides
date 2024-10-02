# Use a Python-based image
FROM python:3.12-slim

# Instalar dependencias del sistema necesarias para compilar catboost
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    cmake \
    libssl-dev \
    libffi-dev \
    libyaml-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalar Cython manualmente antes de las demás dependencias
RUN pip install --no-cache-dir cython

# Copy requirements.txt and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Specify working directory
WORKDIR /app

# Copy application code
COPY . .

# Run the application
CMD ["python", "src/predict.py"]
