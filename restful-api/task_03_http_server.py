#!/usr/bin/python3
"""
This module provides:
    MyHandler class, subclass of
    http.server.BaseHTTPRequestHandler, with:
        do_GET method.
"""


from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    """Handle GET requests depending on the requested path."""
    def do_GET(self):
        """Send a simple text response."""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            pass

server = HTTPServer(("localhost", 8000), MyHandler)
server.serve_forever()
