import requests
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import os
import errno
import shutil
from time import sleep  

fuenteLibro='/home/dgc7/zlibros/libros1920-1921/libro'
descargado=False
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