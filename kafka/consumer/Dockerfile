FROM python:3.12.0
 
WORKDIR /kafka/consumer
 
RUN pip install confluent-kafka pymongo python-dotenv
 
COPY . /kafka/consumer

CMD ["python", "consumer.py"]