import socket
import json
import time
import random
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env variables
PORT = int(os.getenv("Port"))

class SocketServer:

    def __init__(self,port):
        self.PORT = port

        self.ADDR = ("", self.PORT)

        self.FORMAT = 'utf-8'

        # Create a TCP socket using IPv4 addressing
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


        self.server.bind(self.ADDR)

        # Start listening for incoming client connection(producer)
        self.server.listen(1)

    def accept_connection(self):
        self.conn, self.addr = self.server.accept()

    def generate_data(self):
        route = ['Mumbai','Chennai','Bengaluru']
        routefrom = random.choice(route)
        routeto = random.choice(route)

        if routefrom == routeto:
            return None

        data = {
            "Battery_Level":random.randint(1, 100),
            "Device_ID": random.randint(1151, 1153),
            "First_Sensor_temperature": round(random.uniform(10, 40), 1),
            "Route_From": routefrom,
            "Route_To": routeto
        }
        return data

    def send_data(self):
        connected = True
        while connected:
            try:
                for _ in range(5):
                    data = self.generate_data()
                    if not data:
                        continue

                    # Convert the data dictionary to a JSON-formatted string, then encode it to bytes using UTF-8 for transmission
                    userdata = json.dumps(data, indent=1).encode(self.FORMAT)

                    self.conn.send(userdata)
                    time.sleep(100)
            except Exception:
                break

    def close_connection(self):
        self.conn.close()


if __name__ == "__main__":
    server = SocketServer(PORT)
    server.accept_connection()
    server.send_data()
    server.close_connection()
