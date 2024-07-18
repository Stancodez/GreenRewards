from flask import Flask, jsonify, request
from flask_cors import CORS
import pymongo
import os

app = Flask(__name__)
CORS(app)

# MongoDB connection setup
client = pymongo.MongoClient(os.getenv("MONGODB_URI"))
db = client.get_database('GreenRewards')

@app.route('/')
def home():
    return "GreenRewards API"

@app.route('/log_waste', methods=['POST'])
def log_waste():
    data = request.json
    # Code to log waste disposal
    db.waste_logs.insert_one(data)
    return jsonify({"message": "Waste logged successfully"})

if __name__ == "__main__":
    app.run(debug=True)

