from confluent_kafka import Consumer, KafkaError
import pymongo
import json
import os
from dotenv import load_dotenv

# Load environment variables once at module level
load_dotenv(dotenv_path=".env")

# Assign environment variables to constants
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
            "group.id": "my-consumer-group"
        }

        self.consumer = Consumer(self.conf)
        self.consumer.subscribe([TOPIC])



    def process_messages(self):
        while True:
            try:
                msg = self.consumer.poll(1.0)
                
                if msg is None:
                    continue
                    
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        continue
                    continue

                # Process valid message
                json_str = msg.value().decode('utf-8')
                document = json.loads(json_str)
                print(document)
                self.device_data.insert_one(document)
                
            except json.JSONDecodeError:
                continue
            except Exception:
                continue
            finally:
                self.consumer.commit()


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