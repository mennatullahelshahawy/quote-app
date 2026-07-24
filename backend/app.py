from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os
from pathlib import Path  
from dotenv import load_dotenv

base_dir = Path(__file__).resolve().parent.parent
env_path = base_dir / '.env'

load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
CORS(app)

db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")

db = MongoClient(f"mongodb://{db_user}:{db_pass}@{db_host}:27017/{db_name}?authSource=admin")[db_name]

@app.route('/api/quote')
def get_quote():
    doc = list(db.quotes.aggregate([{"$sample": {"size": 1}}]))[0]
    return jsonify({"quote": doc["quote"], "author": doc["author"], "color": doc["color"]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
