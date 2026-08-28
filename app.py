import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import datetime

PORT = int(os.environ.get('APP_PORT', 5000))
LOG_FILE = os.environ.get('LOG_PATH', '/var/log/app/access.log')
ENV = os.environ.get('APP_ENV', 'development')

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{ENV}] {timestamp} - GET {self.path}\n"
        
        try:
            with open(LOG_FILE, 'a') as f:
                f.write(log_entry)
        except Exception as e:
            print(f"Log error: {e}")

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(f'Hello from {ENV} environment!'.encode())

if __name__ == '__main__':
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    print(f"Starting server on port {PORT}...")
    server = HTTPServer(('0.0.0.0', PORT), Handler)
    server.serve_forever()
