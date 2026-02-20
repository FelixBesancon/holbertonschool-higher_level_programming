#!/usr/bin/python3
"""
Simple in-memory RESTful API using Flask.

Endpoints:
- GET  /                : Welcome message.
- GET  /data            : List all usernames.
- GET  /status          : Health check ("OK").
- GET  /users/<username>: Get user object by username.
- POST /add_user        : Add a new user from a JSON payload.
"""


from flask import Flask, request, jsonify

app = Flask(__name__)


users = {}


@app.route("/")
def home():
    """Return a welcome message."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_users():
    """Return the list of all usernames stored in memory."""
    return jsonify(list(users.keys()))


@app.route("/status")
def get_status():
    """Return a simple health-check response."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """
    Return the user object for the given username.

    If the user does not exist, returns a 404 JSON error.
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Add a new user from a JSON payload.

    Expected JSON example:
    {"username": "john", "name": "John", "age": 30, "city": "New York"}

    Errors:
    - 400 Invalid JSON
    - 400 Username is required
    - 409 Username already exists
    """
    user_data = request.get_json(silent=True)

    if user_data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = user_data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    else:
        users[username] = user_data
        return jsonify(
            {
                "message": "User added",
                "user": user_data
            }), 201


if __name__ == "__main__":
    app.run()
