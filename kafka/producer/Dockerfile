FROM python:3.12-slim

WORKDIR /kafka/producer
 
RUN pip install python-dotenv confluent-kafka 
 
COPY . /kafka/producer
 
EXPOSE 6000

CMD ["python", "producer.py"]