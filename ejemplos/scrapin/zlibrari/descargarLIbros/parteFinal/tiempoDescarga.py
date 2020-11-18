
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
def tiempoDescarga():
    fuenteLibro='/home/dgc7/zlibros/libros1920-1921/libro'
    descargado=False
    numeroArchivo=contarNueroArchivos()
    print("esperando la descarga ...")
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
    print("termine",archivos)





def contarNueroArchivos():
    fuenteLibro='/home/dgc7/zlibros/libros1920-1921/libro'
    NumeroDescargas=0
    if os.listdir(fuenteLibro):
        for i in os.listdir(fuenteLibro):
            NumeroDescargas+=1
    return NumeroDescargas


tiempoDescarga()
print(contarNueroArchivos())