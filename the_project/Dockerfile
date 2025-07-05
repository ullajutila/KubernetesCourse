# Use official Python base image
FROM python:3.11-slim

# Ensure stdout/stderr are unbuffered
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy the Python script
COPY server.py .

# Expose the port (optional, for documentation)
EXPOSE 8000

# Start the server
CMD ["python", "server.py"]

