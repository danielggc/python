import socket 
host =socket.gethostname()
port =8058
 

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as coneccion:
    coneccion.connect((host,port))
    datos2=b"hjola pelmaso a estudiar"
    coneccion.sendall(datos2)
    mensajeResivido=coneccion.recvfrom(1024)

print('\n resivido2',mensajeResivido[0])