#!/usr/bin/python3
"""
Task 05 - API Security and Authentication Techniques

This module implements:
- Basic Authentication using Flask-HTTPAuth
- JWT Authentication using Flask-JWT-Extended
- Role-based access control
"""

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
auth = HTTPBasicAuth()

# JWT Configuration
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)


# In-memory user storage
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
    """
    Verify user credentials for Basic Authentication.
    Returns the user object if authentication succeeds,
    otherwise returns None.
    """
    if username in users and check_password_hash(
            users[username]["password"], password):
        return users[username]
    return None


@app.route("/basic-protected")
@auth.login_required
def basic_auth():
    """
    Basic Authentication protected route.
    Accessible only with valid Basic credentials.
    """
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """
    Authenticate user and return a JWT access token
    if credentials are valid.
    """
    data = request.get_json()
    # Login logic to be implemented


if __name__ == "__main__":
    app.run()
