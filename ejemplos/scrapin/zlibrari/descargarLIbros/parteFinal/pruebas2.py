import re
def guardarHistorial(_añoX,_añoY,_paginas):
    dirRegistroDescargas='/home/dgc7/Documentos/zlibrary/registro/registroDescargas.txt'
    datoAñosF=open(dirRegistroDescargas,'r')
    contador=0
    lista=[]
    paginash=_paginas
    añoXh=_añoX
    añoYh=_añoY
    for datos in re.split('\n',str(datoAñosF.read())):
        contador+=1
        if contador <5:
            respaldoh=datos
    lista.append(añoXh)
    print(paginash)
    lista.append(añoYh)
    lista.append(paginash)
    lista.append(respaldoh)
    datoAñosF.close()
    datoAñosF=open(dirRegistroDescargas,'w')
    datoAñosF.close()
    datoAñosF=open(dirRegistroDescargas,'r+')
    for a in range(0,4):
        datoAñosF.write(str(lista[a])+'\n')

def datosDescarga(_indicador):
    indicador=_indicador
    dirRegistroDescargas='/home/dgc7/Documentos/zlibrary/registro/registroDescargas.txt'
    datoAños=open(dirRegistroDescargas,'r')
    contador=0
    for i in datoAños.readlines():
        contador+=1
        if indicador==contador:
            dato=i
    datoAños.close()
    return int(dato)



def usuarioUsadosLeer():
    dirRegistroDescargas='/home/dgc7/Documentos/zlibrary/registro/registroUsuario.txt'
    datosAñosU=open(dirRegistroDescargas,'r')
    datosUsuarios=int(datosAñosU.readline())
    return datosUsuarios



añoX=datosDescarga(1)
añoY=datosDescarga(2)
conteoPagina=datosDescarga(3)

for i in range(0,3):
    añoY+=1
    añoX+=1
    print(añoX,añoY)
    guardarHistorial(añoX,añoY,conteoPagina)
