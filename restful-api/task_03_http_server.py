#!/usr/bin/python3
"""
This module provides:
    MyHandler class, subclass of
    http.server.BaseHTTPRequestHandler, with:
        do_GET method.
"""


from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    """Handle HTTP GET requests."""
    def do_GET(self):
        """Send a simple text response."""
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple API!")

server = HTTPServer(("localhost", 8000), MyHandler)
server.serve_forever()
