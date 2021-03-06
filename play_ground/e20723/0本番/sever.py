#!/usr/bin/env python3

import socket
import pickle

HOST = socket.gethostbyname(socket.gethostname())  # Standard loopback interface address (localhost)
PORT = 49152   # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(pickle.dumps(""))
            print(pickle.loads(data))
