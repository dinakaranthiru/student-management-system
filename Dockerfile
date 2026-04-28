# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

# Set work directory
WORKDIR /app

# Install system dependencies for MySQL
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    pkg-config \
    gcc \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Give execution permissions to start.sh
RUN chmod +x /app/start.sh

# Expose port
EXPOSE 8000

# Run the startup script
CMD ["/app/start.sh"]
