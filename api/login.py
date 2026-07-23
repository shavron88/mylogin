from http.server import BaseHTTPRequestHandler
import json


class handler(BaseHTTPRequestHandler):

    def do_POST(self):

        content_length = int(self.headers["Content-Length"])

        body = self.rfile.read(content_length)

        data = json.loads(body)

        username = data.get("username")
        password = data.get("password")


        if username == "admin" and password == "password":

            response = {
                "success": True
            }

            self.send_response(200)

        else:

            response = {
                "success": False,
                "message": "Invalid username or password"
            }

            self.send_response(401)


        self.send_header(
            "Content-type",
            "application/json"
        )

        self.end_headers()

        self.wfile.write(
            json.dumps(response).encode()
        )