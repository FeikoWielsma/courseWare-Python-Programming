# server.py
import socket
import time

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

while True:
    # establish a connection
    print("Accepting connections")
    clientsocket, addr = serversocket.accept()

    print("Got a connection from %s" % str(addr))
    current_time = time.ctime(time.time()) + "\r\n"
    clientsocket.send(current_time.encode("ascii"))
    clientsocket.close()
