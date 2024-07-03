from flask import request, jsonify
from app import app, mongo
from flask_jwt_extended import create_access_token, jwt_required

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    existing_user = mongo.db.users.find_one({"email": email})
    
    if existing_user:
        return jsonify({"msg": "User already exists"}), 400
    
    create_user(data['username'], email, data['password'])
    return jsonify({"msg": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = find_user_by_email(data['email'])
    
    if user and user['password'] == data['password']:
        access_token = create_access_token(identity=user['email'])
        return jsonify(access_token=access_token), 200
    
    return jsonify({"msg": "Bad email or password"}), 401

@app.route('/wastelog', methods=['POST'])
@jwt_required()
def log_waste():
    data = request.get_json()
    email = get_jwt_identity()
    user = find_user_by_email(email)
    
    if user:
        mongo.db.wastelogs.insert_one({
            "user_id": user["_id"],
            "type": data["type"],
            "method": data["method"],
            "location": data["location"],
            "timestamp": datetime.utcnow()
        })
        mongo.db.users.update_one(
            {"_id": user["_id"]},
            {"$inc": {"points": 10}}
        )
        return jsonify({"msg": "Waste log added and points updated"}), 201
    
    return jsonify({"msg": "User not found"}), 404

