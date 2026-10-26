import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

from loan import monthly_payment

PORT = 8000


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urlparse(self.path)
        if url.path == "/healthz":
            self.reply(200, {"status": "ok"})
        elif url.path == "/payment":
            q = parse_qs(url.query)
            try:
                payment = monthly_payment(
                    float(q["amount"][0]),
                    float(q["rate"][0]),
                    int(q["months"][0]),
                )
                self.reply(200, {"payment": payment})
            except (KeyError, ValueError) as err:
                self.reply(400, {"error": str(err)})
        else:
            self.reply(404, {"error": "not found"})

    def reply(self, code, body):
        data = (json.dumps(body) + "\n").encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


if __name__ == "__main__":
    print(f"loan-api listening on port {PORT}", flush=True)
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()