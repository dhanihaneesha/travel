# Use official Python base image
FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Install dependencies system-wide for better speed
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy app files
COPY app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY app /app

# Expose port used by Flask
EXPOSE 5000

# Use gunicorn for production-style server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--workers", "3"]
