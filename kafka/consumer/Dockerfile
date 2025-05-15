FROM python:3.12-slim
 
WORKDIR /kafka/consumer
 
RUN pip install confluent-kafka pymongo python-dotenv
 
COPY . /kafka/consumer

CMD ["python", "consumer.py"]