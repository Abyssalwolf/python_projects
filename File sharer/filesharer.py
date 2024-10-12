import http.server
import socketserver
import socket
import webbrowser

import pyqrcode
from pyqrcode import QRCode

import png
import os

PORT=8010
os.environ['USERPROFILE']
downloads = os.path.join(os.path.join(os.environ['USERPROFILE']),
                       'Downloads')
os.chdir(downloads)

Handler=http.server.SimpleHTTPRequestHandler

hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)
link = "http://" + IP + ":" + str(PORT)

url=pyqrcode.create(link)
url.svg("myqr.svg",scale=8)
webbrowser.open("myqr.svg")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    print("Type this in your Browser", IP)
    print("or Use the QRCode")
    httpd.serve_forever()