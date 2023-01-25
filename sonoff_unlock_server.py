from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        buffer = []
        buffer.append(b"HTTP/1.1 200 OK\r\n")
        buffer.append(b"Server: openresty\r\n")
        buffer.append(b"Date: Mon, 23 Jan 2023 19:47:42 GMT\r\n")
        buffer.append(b"Content-Type: application/json\r\n")
        buffer.append(b"Content-Length: 14\r\n")
        buffer.append(b"Connection: close\r\n")
        buffer.append(b"\r\n")
        buffer.append(b"{\"error\": 422}\r\n")
        self.wfile.write(b"".join(buffer))
        self.wfile.flush()

httpd = HTTPServer(("", 8081), SimpleHTTPRequestHandler)
httpd.serve_forever()
