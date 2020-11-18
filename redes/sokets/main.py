#!/usr/bin/env python
import socket
host= socket.gethostname()
port=8051
BUFFER_SIZE=1024


with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as socket_tcp:
    socket_tcp.bind((host,port))
    socket_tcp.listen(5)
    conn,adde=socket_tcp.accept()
    with conn :
        while True:
            data=conn.recv(BUFFER_SIZE)
            if not data:
                print("holas")
                break
            else:
                print('[*] Datos recibidos: {}'.format(data.decode('utf-8'))) 