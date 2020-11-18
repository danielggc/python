import socket
host= socket.gethostname()
port=8058
BUFFER_SIZE=1024


with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as socket_tcp:
    socket_tcp.bind((host,port))
    socket_tcp.listen(5)
    conn,adde=socket_tcp.accept()
    with conn :
        while True:
            data=conn.recv(BUFFER_SIZE)
            if not data:
                break
            else:
                print('[*] Datos recibidos: ',repr(data)) 
                conn.sendall(b"hola daniel como estas por que te demoras tanto")
                socket_tcp.close()