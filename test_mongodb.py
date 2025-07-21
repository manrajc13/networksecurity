from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("MONGODB_URL")

# Nuclear option - completely disable SSL verification

client = MongoClient(url)

try:
    client.admin.command('ping')
    print("Connected to MongoDB!")
except Exception as e:
    print(f"Still failed: {e}")