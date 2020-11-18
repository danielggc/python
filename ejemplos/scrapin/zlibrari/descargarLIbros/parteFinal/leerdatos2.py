import re
import shutil
import re
import random
from unicodedata import normalize
import csv
import requests
import wget
import shutil
import os
import errno
import unittest
from bs4 import BeautifulSoup
from time import sleep
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
            print(datos)            
    lista.append(añoXh)
    lista.append(añoYh)
    lista.append(paginash)
    lista.append(respaldoh)
    datoAñosF.close()
    datoAñosF=open(dirRegistroDescargas,'w')
    datoAñosF.close()
    datoAñosF=open(dirRegistroDescargas,'r+')
    for a in range(0,4):
        datoAñosF.write(str(lista[a])+'\n')
    print("aa",respaldoh)


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

def guardarNumeroDescargas(_numeroDescargas):
    dirRegistroDescargas='/home/dgc7/Documentos/zlibrary/registro/registroDescargas.txt'
    datoAñosF=open(dirRegistroDescargas,'r')
    contador=0
    lista=[]
    nuemroDescargas=_numeroDescargas
    for datos in re.split('\n',str(datoAñosF.read())):
        contador+=1
        if contador <4:
            lista.append(datos)
    lista.append(nuemroDescargas)
    datoAñosF.close()
    datoAñosF=open(dirRegistroDescargas,'w')
    datoAñosF.close()
    datoAñosF=open(dirRegistroDescargas,'r+')
    for a in range(0,4):
        datoAñosF.write(str(lista[a])+'\n')

def usuarioUsadosLeer():
    dirRegistroDescargas='/home/dgc7/Documentos/zlibrary/registro/registroUsuario.txt'
    datosAñosU=open(dirRegistroDescargas,'r')
    datosUsuarios=int(datosAñosU.readline())
    return datosUsuarios


def usuarioUsadosReescrivir(_usuariUsados):
    usuariUsados =_usuariUsados
    dirRegistroDescargas='/home/dgc7/Documentos/zlibrary/registro/registroUsuario.txt'
    datosAñosU=open(dirRegistroDescargas,'w+')
    datosAñosU.write(str(usuariUsados))

def contarNueroArchivos():
    fuenteLibro='/home/dgc7/zlibros/libros1920-1921/libro'
    NumeroDescargas=0
    for i in os.listdir(fuenteLibro):
        NumeroDescargas+=1
    return NumeroDescargas

def tiempoDescarga():
    fuenteLibro='/home/dgc7/zlibros/libros1920-1921/libro'
    descargado=False
    numeroArchivo=contarNueroArchivos()
    print("estoy esperando que descargue")
    while numeroArchivo >1:
        numeroArchivo=contarNueroArchivos()
    sleep(2)
    archivos= os.listdir(fuenteLibro)
    print(archivos)
    while descargado==False:
        if re.search('Sin|sin',str(archivos)):
            if re.search('confirmar|Confirmar',str(archivos)):
                sleep(0.1)
            else:
                descargado=True
        else:
            if re.search('Unconfirmed|unconfirmed',str(archivos)):
                sleep(0.1)
            else:
                descargado=True
        archivos=os.listdir(fuenteLibro)
    print("termine las descarga ",archivos)


#usuarioUsadosReescrivir(2)
#print(usuarioUsadosLeer())
#guardarHistorial(1920,1921,1)
#print(datosDescarga(4))
#guardarNumeroDescargas(5)
tiempoDescarga()
