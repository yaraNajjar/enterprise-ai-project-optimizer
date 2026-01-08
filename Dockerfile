# Use official Python 3.13 image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into container
COPY . .

# Expose the port for FastAPI
EXPOSE 8000

# Command to run API
CMD ["python", "-m", "uvicorn", "ml.api:app", "--host", "0.0.0.0", "--port", "8000"]
