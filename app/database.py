from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI=os.getenv("MONGO_URI")


client =MongoClient(MONGO_URI)
db = client['scm_database']
users_data = db['users_data']
shipment_data = db['shipment_data']
device_data = db['device_data']
