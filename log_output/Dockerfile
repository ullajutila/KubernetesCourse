# Use a minimal Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy script into the container
COPY logoutput.py .

# Set default command
CMD ["python", "-u", "logoutput.py"]
