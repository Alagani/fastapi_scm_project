# Use a slim version of the official Python 3.12 image as the base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /kafka/consumer

# Install required Python packages globally
# - confluent-kafka: Kafka client for Python
# - pymongo: MongoDB driver
# - python-dotenv: To load environment variables from a .env file
RUN pip install confluent-kafka pymongo python-dotenv

# Copy all project files from the host into the working directory in the container
COPY . .

# Set the default command to run the Kafka consumer script
CMD ["python", "consumer.py"]
