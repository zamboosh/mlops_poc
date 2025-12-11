# Dockerfile

# --- STAGE 1: Build Environment ---
# Use a Python base image. The slim version is recommended for smaller size.
FROM python:3.10-slim AS builder

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies needed for Python libraries
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    # Clean up to reduce image size
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy only the requirements file first to take advantage of Docker layer caching
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip
# This is the crucial change:
# Use --index-url to point to PyTorch's CPU-only index.
RUN pip install --no-cache-dir \
    -r requirements.txt \
    --index-url https://download.pytorch.org/whl/cpu \
    --extra-index-url https://pypi.org/simple

# --- STAGE 2: Final Image (Security and Size Optimized) ---
# Start from a clean, smaller base for the final runtime
FROM python:3.10-slim

# Set the working directory again
WORKDIR /app

# Copy the installed libraries from the builder stage
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy the application code
COPY app.py .

# Set environment variables for Gunicorn/Uvicorn
ENV PORT=8080
ENV HOST=0.0.0.0

# Expose the port on which the application will run
EXPOSE 8080

# Command to run the application using Uvicorn (a high-performance ASGI server)
# Use gunicorn with uvicorn workers for production stability and parallelism
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]