#!/usr/bin/env python3

import socket
import pickle

HOST = socket.gethostbyname(socket.gethostname())
print(HOST)  # The server's hostname or IP address
PORT = 49152        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(pickle.dumps("目駅"))
    data = s.recv(1024)

print('Received', pickle.loads(data))
