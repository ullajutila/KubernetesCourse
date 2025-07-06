import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

def main():
    port = int(os.environ.get("PORT", 8000))  # Default port if not set
    web_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(web_dir)  # Ensure server serves from current script directory

    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Server started in port {port}", flush=True)
    httpd.serve_forever()

if __name__ == "__main__":
    main()

