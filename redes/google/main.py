import socket
host=socket.gethostbyname('www.google.com') 
print(host)
port=socket.getservbyname('http')
print(port)
print("crean un soket")
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket creado")
print("conectadose al  remoto host")
client.connect((host,80))
print("connectado")
client.send(b"GET /index.html HTML/1.1\r\n\r\n")
data=client.recv(1024)
1if data=="":
    print("no hay nada")
else :
    print(data)