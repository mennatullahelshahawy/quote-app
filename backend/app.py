from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

db = MongoClient("mongodb://root:example@localhost:27017/quotes-app?authSource=admin")["quotes-app"]

@app.route('/api/quote')
def get_quote():
    doc = list(db.quotes.aggregate([{"$sample": {"size": 1}}]))[0]
    return jsonify({"quote": doc["quote"], "author": doc["author"], "color": doc["color"]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
