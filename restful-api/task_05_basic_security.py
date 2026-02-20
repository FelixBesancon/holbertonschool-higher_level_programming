#!/usr/bin/python3
"""
"""


from flask import Flask
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import WTManager, create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("MyPassword1234"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("MyPassword"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_user(username, password):
    """"""
    if username in users and check_password_hash(users[username]["password"], password):
        return users[username]
    return None


@app.route("/basic-protected")
@auth.login_required
def basic_auth():
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def gat


@app.route("/jwt-protected")


if __name__ == "__main__":
    app.run()
