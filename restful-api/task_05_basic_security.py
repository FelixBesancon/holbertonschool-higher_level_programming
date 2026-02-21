#!/usr/bin/python3
"""
API Security and Authentication Techniques.

This module provides a Flask-based REST API that demonstrates:
    Basic HTTP Authentication using Flask-HTTPAuth.
    Token-based authentication using JSON Web Tokens (JWT).
    Role-based access control (RBAC).
    Custom JWT error handling with consistent 401 responses.

The API includes:
    A Basic Auth protected endpoint.
    A login endpoint that generates JWT access tokens.
    JWT-protected routes.
    An admin-only route restricted by user role.

User credentials are stored in memory with hashed passwords.
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

app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)


users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
        },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
        }
}


@auth.verify_password
def verify_user(username, password):
    """
    Validate user credentials for Basic Authentication.

    Args:
        username (str): Username provided in the Authorization header.
        password (str): Plain text password provided by the client.

    Returns:
        dict: The user dictionary if authentication succeeds.
        None: If the username does not exist or the password is incorrect.
    """
    if username in users and check_password_hash(
            users[username]["password"], password):
        return users[username]
    return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_auth():
    """
    Basic Authentication protected endpoint.

    This route requires valid Basic HTTP credentials.
    If authentication succeeds, access is granted.

    Returns:
        str: "Basic Auth: Access Granted"
        HTTP 401: If credentials are missing or invalid.
    """
    return "Basic Auth: Access Granted"


@auth.error_handler
def basic_auth_error():
    """
    Handle Basic Authentication errors.

    Returns:
        JSON response with error message and 401 status code.
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.route("/login", methods=["POST"])
def login():
    """
    Authenticate a user and generate a JWT access token.

    Expects a JSON payload:
        {
            "username": "<username>",
            "password": "<password>"
        }

    Returns:
        JSON: {"access_token": "<JWT_TOKEN>"} with HTTP 200,
        if credentials are valid.
        JSON: {"error": "..."} with HTTP 401 if authentication fails.
    """
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 401

    data = request.get_json()

    if data is None:
        return jsonify({"error": "Missing username:password"}), 401

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Invalid credentials"}), 401

    user = users.get(username)

    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    if check_password_hash(user["password"], password) is False:
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(
        identity=username,
        additional_claims={"role": user["role"]}
        )

    return jsonify({"access_token": access_token})


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """
    JWT-protected endpoint.

    Requires a valid JWT access token in the Authorization header:
        Authorization: Bearer <token>

    Returns:
        str: "JWT Auth: Access Granted" if token is valid.
        HTTP 401: If token is missing, invalid, or expired.
    """
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """
    Role-based protected endpoint (admin only).

    Requires a valid JWT access token.
    Grants access only if the authenticated user's role is "admin".

    Returns:
        str: "Admin Access: Granted" with HTTP 200 if user is admin.
        JSON: {"error": "Admin access required"} with HTTP 403,
        if user is not admin.
        HTTP 401: If token is missing, invalid, or expired.
    """
    username = get_jwt_identity()
    user = users.get(username)

    if not user:
        return jsonify({"error": "Missing or invalid token"}), 401

    if user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(_error):
    """
    Handle missing JWT token errors.

    Triggered when a protected route is accessed
    without providing a valid Authorization header.

    Returns:
        JSON response with error message and 401 status code.
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(_error):
    """
    Handle invalid JWT token errors.

    Triggered when the provided token is malformed
    or cannot be decoded properly.

    Returns:
        JSON response with error message and 401 status code.
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(_jwt_header, _jwt_payload):
    """
    Handle expired JWT token errors.

    Triggered when the provided token has passed
    its expiration time.

    Returns:
        JSON response with error message and 401 status code.
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(_jwt_header, _jwt_payload):
    """
    Handle revoked JWT token errors.

    Triggered when the token has been explicitly
    revoked or blacklisted.

    Returns:
        JSON response with error message and 401 status code.
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(_jwt_header, _jwt_payload):
    """
    Handle fresh token requirement errors.

    Triggered when a route requires a fresh token
    but a non-fresh token was provided.

    Returns:
        JSON response with error message and 401 status code.
    """
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
