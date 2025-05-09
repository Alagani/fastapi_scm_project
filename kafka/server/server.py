import socket
import errno
import json
import time
import random
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env variables
PORT = int(os.getenv("Port"))  # Assign before class, can override via constructor

class SocketServer:

    def __init__(self,port):
        self.PORT = port
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.ADDR = ("", self.PORT)
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MESSAGE = "!DISCONNECT"

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)
        self.server.listen(2)

    def accept_connection(self):
        self.conn, self.addr = self.server.accept()

    def generate_data(self):
        route = ['Newyork, USA', 'Chennai, India', 'Bengaluru, India', 'London, UK']
        routefrom = random.choice(route)
        routeto = random.choice(route)

        if routefrom == routeto:
            return None

        data = {
            "Battery_Level": round(random.uniform(2.00, 5.00), 2),
            "Device_ID": random.randint(1150, 1158),
            "First_Sensor_temperature": round(random.uniform(10, 40.0), 1),
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

                    userdata = json.dumps(data, indent=1).encode(self.FORMAT)
                    self.conn.send(userdata)
                    time.sleep(10)

            except IOError as e:
                if e.errno == errno.EPIPE:
                    break
            except Exception:
                break

    def close_connection(self):
        self.conn.close()


if __name__ == "__main__":
    server = SocketServer(PORT)
    server.accept_connection()
    server.send_data()
    server.close_connection()
