import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

def main():
    port = int(os.environ.get("PORT", 8000))  # Default to 8000 if PORT not set
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Server started in port {port}", flush=True)
    httpd.serve_forever()

if __name__ == "__main__":
    main()

