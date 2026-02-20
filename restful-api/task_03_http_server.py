#!/usr/bin/python3
"""
Simple HTTP API built using http.server.

Endpoints:
    GET /        -> Returns a welcome message (text/plain)
    GET /data    -> Returns sample JSON data (application/json)
    GET /status  -> Returns API status (text/plain)
    GET /info    -> Returns API information (application/json)
    Any other    -> Returns 404 Not Found
"""


from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class MyHandler(BaseHTTPRequestHandler):
    """
    Custom request handler for the simple API.

    Handles GET requests and routes them
    according to the requested path.
    """
    def do_GET(self):
        """
        Process GET requests and send the appropriate response
        based on the requested endpoint.
        """

        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode())

        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json_data.encode())

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write("OK".encode())

        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
                }
            info_json = json.dumps(info)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(info_json.encode())

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write("Endpoint not found".encode())


server = HTTPServer(("localhost", 8000), MyHandler)
server.serve_forever()
