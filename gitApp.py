from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi
import sqlite3
import json

class Guitar():
    def __init__(self, mfr, mdl, gtype, puc, color):
        self.gId = None  # We're auto-incrementing this
        self.mfr = mfr  # manufactuer: 'Gibson'
        self.mdl = mdl  # model: 'SG'
        self.gtype = gtype  # guitar type: 'electric'
        self.puc = puc  # pickup configuration: 'HH'
        self.color = color  # i.e. 'ebony'

class GittyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith("/all"):
            self.send_response(200)
            self.send_header('content_type', 'application/json')
            self.end_headers()
            conn = sqlite3.connect('gitty.db')
            cursor = conn.cursor()
            query = "SELECT * FROM guitars"
            result = cursor.execute(query)
            rows = result.fetchall()
            items = []
            for row in rows:
                lr = list(row)
                gitty = Guitar(*lr)
                items.append({"gId": gitty.gId, "mfr": gitty.mfr,
                              "mdl": gitty.mdl, "gtype": gitty.gtype,
                              "puc": gitty.puc, "color": gitty.color})
            for item in items:
                    self.wfile.write(json.dumps(item).encode())

    def do_POST(self):
        if self.path.endswith("/add_new"):
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            content_len = int(self.headers.get('Content-length'))
            pdict['CONTENT-LENGTH'] = content_len
            if ctype == 'application/json':
                payload = json.loads(self.rfile.read(content_len))
                gitty = Guitar(*payload.values())
                try:
                    conn = sqlite3.connect('gitty.db')
                    cursor = conn.cursor()    
                    query = "INSERT INTO guitars (mfr, mdl, gtype, puc, color) VALUES (?, ?, ?, ?, ?)"
                    cursor.execute(query, (gitty.mfr, gitty.mdl, gitty.gtype, gitty.puc, gitty.color))
                    conn.commit()
                    self.send_response(201)
                    self.send_header('content-type', 'application/json')
                    self.send_header('Location', '/add_new')
                    self.end_headers()
                except sqlite3.Error as er:
                    print("SQLite Error: {}".format(er))
                    self.send_response(500)
                    self.send_header('content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write("Your G string broke...".encode())


def main():
    PORT = 9191
    server = HTTPServer(('', PORT), GittyHandler)
    print('SERVER RUNNING ON PORT:{}'.format(PORT))
    server.serve_forever()

if __name__ == "__main__":
    main()
