from app import mongo

def create_user(username, email, password):
    user = {
        "username": username,
        "email": email,
        "password": password,
        "points": 0
    }
    mongo.db.users.insert_one(user)

def find_user_by_email(email):
    return mongo.db.users.find_one({"email": email})

