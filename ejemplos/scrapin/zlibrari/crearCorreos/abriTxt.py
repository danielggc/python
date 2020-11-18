import re
from unicodedata import normalize

dirNombre='/home/dgc7/ejersiciosLibros/pyaton/ejemplos/scrapin/zlibrari/crearCorreos/nombre.txt'
nombre=open(dirNombre,'r+')
dirapellido='/home/dgc7/ejersiciosLibros/pyaton/ejemplos/scrapin/zlibrari/crearCorreos/apellidos.txt'
apellido=open(dirapellido,'r+')
dirContrasenna='/home/dgc7/ejersiciosLibros/pyaton/ejemplos/scrapin/zlibrari/crearCorreos/contraseña.txt'
contrasenna=open(dirContrasenna,'r+')
dirCotrasenna2='/home/dgc7/ejersiciosLibros/pyaton/ejemplos/scrapin/zlibrari/crearCorreos/contraseña2.txt'
Contrasenna2=open(dirCotrasenna2,'r+')
datosContrasenna=[]
lista=[]

tildes=['á','é','í','ó','ú']
suptildes=['a','e','i','o','u']

for d in range(0,102):
    lista.append(nombre.readline()+apellido.readline())
    datosContrasenna.append(contrasenna.readline()+Contrasenna2.readline())
    print(contrasenna.readline()+Contrasenna2.readline())
    print(nombre.readline()+apellido.readline())

for d in range(0,101):
    posicion2=d+1
    lista[d]=re.sub('\n','asdaawderca',lista[d])
    datosContrasenna[d]=re.sub('\n','radabanals',datosContrasenna[d])
    lista[d]=re.sub(
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
        normalize( "NFD",lista[d]), 0, re.I
    )
    lista[d]= normalize( 'NFC',lista[d])
    datosContrasenna[d]=re.sub(
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
        normalize( "NFD",datosContrasenna[d]), 0, re.I
    )
    datosContrasenna[d]= normalize( 'NFC',lista[d])
    lista2='https://maildrop.cc/inbox/'+lista[d]
    lista[d]='@maildrop.cc'
    print(lista[d])
    print('\n')
    print(datosContrasenna[d])   


    import re
from unicodedata import normalize


