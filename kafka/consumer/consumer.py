from confluent_kafka import Consumer
import pymongo
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Assign environment variables
MONGODB_URI = os.getenv("MONGODB_URI")
MONGODB_DATABASE = os.getenv("MONGODB_DATABASE")
BOOTSTRAP_SERVERS = os.getenv("bootstrap_servers")
TOPIC = os.getenv("topic")

class KafkaMongoConsumer:

    def __init__(self):
        # MongoDB setup
        self.client = pymongo.MongoClient(MONGODB_URI)

        self.db = self.client[MONGODB_DATABASE]

        self.device_data = self.db["device_data"]

        # Consumer configuration
        self.conf = {
            'bootstrap.servers': BOOTSTRAP_SERVERS,
            'group.id': 'my-consumer-group',
            'enable.auto.commit': True,
            'auto.commit.interval.ms': 5000     # Automatically commit offsets to every 5 seconds
        }


        self.consumer = Consumer(self.conf)
        self.consumer.subscribe([TOPIC])



    def process_messages(self):
        while True:
            try:


                msg = self.consumer.poll(1.0)
                
                if msg is None:
                    continue
                    
                elif msg.error():
                    continue

                json_str = msg.value().decode('utf-8')     # Convert binary Kafka message to JSON string
                document = json.loads(json_str)            # Convert JSON string to Python dictionary
                self.device_data.insert_one(document)


            except Exception:
                continue


    def close_consumer(self):
        self.consumer.close()
        self.client.close()


if __name__ == "__main__":
    consumer = KafkaMongoConsumer()

    try:
        consumer.process_messages()
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close_consumer()