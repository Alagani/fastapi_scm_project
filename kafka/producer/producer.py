import socket
from confluent_kafka import Producer
import os
from dotenv import load_dotenv

# Load environment variables once at module level
load_dotenv()

# Assign environment variables to module-level constants
BOOTSTRAP_SERVERS = os.getenv('bootstrap_servers')
HOST = os.getenv('host')
PORT = int(os.getenv('port'))
TOPIC = os.getenv('topic')

class KafkaSocketProducer:

    def __init__(self):
        # Kafka configuration using pre-loaded env vars
        self.producer_config = {
            'bootstrap.servers': BOOTSTRAP_SERVERS
        }
        self.producer = Producer(self.producer_config)
        
        # Socket configuration
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.settimeout(5)



    def connect_to_server(self):
        """Connect to the TCP server using pre-loaded host and port"""
        self.server.connect((HOST, PORT))



    def receive_message(self):
        """Receive a single message from the socket server"""
        try:
            message = self.server.recv(1024).decode('utf-8')
            return message if message else None
        except socket.timeout:
            return None
        except (ConnectionResetError, Exception):
            return False  # Signal connection error



    def produce_message(self, message):
        """Produce a message to Kafka using pre-loaded topic"""
        print(message)
        self.producer.produce(
            TOPIC,
            key="key",
            value=message
        )
        self.producer.poll(0.1)



    def process_messages(self):
        """Main processing loop that receives and produces messages"""
        try:
            while True:
                message = self.receive_message()
                
                if message is False:
                    break  # Connection error occurred
                elif message:
                    self.produce_message(message)
        except KeyboardInterrupt:
            pass



    def close_connections(self):
        """Ensure all connections are properly closed"""
        if self.producer:
            self.producer.flush()  # Flush pending messages
        if self.server:
            self.server.close()




if __name__ == "__main__":
    producer = KafkaSocketProducer()

    try:
        producer.connect_to_server()
        producer.process_messages()
    finally:
        producer.close_connections()