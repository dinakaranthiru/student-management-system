# Use Azure's official Python image (No Docker Hub needed!)
FROM mcr.microsoft.com/oryx/python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

# Set work directory
WORKDIR /app

# Ultimate Fix: Remove all broken Microsoft repo links from all sources
RUN sed -i '/packages.microsoft.com/d' /etc/apt/sources.list.d/* 2>/dev/null || true && \
    apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    pkg-config \
    gcc \
    dos2unix \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*
# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Give execution permissions to start.sh and fix line endings
RUN dos2unix /app/start.sh && chmod +x /app/start.sh

# Expose port
EXPOSE 8000

# Run the startup script
CMD ["/app/start.sh"]
