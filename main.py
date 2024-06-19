import socket
import threading
from parsers.httpParser import parseHTTPRequest
from urlMapper.urlServer import returnFiles

def handleClient(clientsocket: socket, clientaddr):
    req = clientsocket.recv(4096)
    parsed = parseHTTPRequest(req.decode())
    data = returnFiles(parsed)


    res = f'''HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: {len(data)}
Connection: close

{data}'''
    clientsocket.send(res.encode())




sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8002))
sock.listen(5)

while True:

    (clientsocket, address) = sock.accept()

    thd = threading.Thread(target=handleClient, args=(clientsocket, address))
    thd.start()
