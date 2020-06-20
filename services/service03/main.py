import json
from http.server import HTTPServer, BaseHTTPRequestHandler


class ServiceHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        response = json.dumps({'message': 'Hello from service 3'})
        self.wfile.write(response.encode('utf8'))


if __name__ == '__main__':
    print('Listening on port 8000')
    server = HTTPServer(('0.0.0.0', 8000), ServiceHandler)
    server.serve_forever()