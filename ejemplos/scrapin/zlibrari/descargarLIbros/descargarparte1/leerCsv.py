import csv
import re
dir='/home/dgc7/ejersiciosLibros/pyaton/ejemplos/scrapin/zlibrari/descargarLIbros/descargarparte1/contraseñasYcorreos.txt'
data=open(dir,'r+')
usuario=[]
contraseña=[]
for i in range(0,200):
    if i%2==0 :
        usuario.append(data.readline())
    if i%2 !=0:
        contraseña.append(data.readline())

for i in range (0,100):
    print(usuario[i])    
    print(contraseña[i])