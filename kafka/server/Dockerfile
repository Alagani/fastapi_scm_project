# Use the official slim Python 3.12 image as the base
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /kafka/server

# Install required Python packages
RUN pip install python-dotenv

# Copy all project files into the container
COPY . .

# Expose port 6000 (server listens on this port)
EXPOSE 6000

# Default command to run your Kafka server script
CMD ["python", "server.py"]
