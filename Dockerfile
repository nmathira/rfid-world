# Use an ARM-compatible Python base image
FROM python:3.11-slim

# Create a working directory
WORKDIR /app

# Copy requirements first (better for caching)
COPY requirements.txt .

# Install dependencies (FastAPI, Uvicorn, etc.)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Run app with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

