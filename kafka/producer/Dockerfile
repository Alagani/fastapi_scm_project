# Use the official slim Python 3.12 image as the base
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /kafka/producer

# Install required Python packages
# - python-dotenv: for loading environment variables from a .env file
# - confluent-kafka: Kafka client for producing messages
RUN pip install python-dotenv confluent-kafka

# Copy all files from the local project directory to the container
COPY . .

# Expose port 6000 (producer listens on this port)
EXPOSE 6000 

# Set the default command to run the Kafka producer script
CMD ["python", "producer.py"]
