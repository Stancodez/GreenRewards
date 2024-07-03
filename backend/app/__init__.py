from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/greenrewards"
app.config["JWT_SECRET_KEY"] = "your_secret_key"

CORS(app)
mongo = PyMongo(app)
jwt = JWTManager(app)

from app import routes

if __name__ == '__main__':
    app.run(debug=True)

