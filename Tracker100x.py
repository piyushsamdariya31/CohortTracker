import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run():
    os.chdir(DIRECTORY)
    url = f"http://localhost:{PORT}/Tracker100x.html"
    print(f"Cohort Tracker server started. Opening in browser: {url}")
    webbrowser.open(url)
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            httpd.serve_forever()
    except OSError as e:
        # If port 8000 is in use, try port 8080
        if e.errno == 10048 or e.errno == 98:
            alt_port = 8080
            url_alt = f"http://localhost:{alt_port}/Tracker100x.html"
            print(f"Port {PORT} busy, starting on port {alt_port}: {url_alt}")
            webbrowser.open(url_alt)
            with socketserver.TCPServer(("", alt_port), Handler) as httpd:
                httpd.serve_forever()
        else:
            raise e

if __name__ == "__main__":
    run()