import requests
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import os
import errno
import shutil

#https://b-ok.cc/book/2037780/65ab73
#http://dl247.zlibcdn.com/dtoken/f755f92b786e73408b8bc16b7b3c3388
#https://b-ok.cc/book/689543/6d01f9
url='https://b-ok.cc/dl/3620695/85911b'
html=requests.get(url)
soup=BeautifulSoup(html.content,'html.parser')
titulo=soup.find_all(class_="moderatorPanelToggler")
titulo=re.sub('</h1>]',' ',str(titulo))
respaldo=re.split('>',titulo)
titulo=respaldo[1]
if re.split(':',titulo):
    respaldo=re.split(':',titulo)
    titulo=respaldo[0]
    if re.split('\w',titulo):
        respaldo=re.split('\w',titulo,1)
        titulo=respaldo[1]
        if re.split('   ',titulo):
            respaldo=re.split('   ',str(titulo))
            titulo=respaldo[0]
        respaldo=re.sub(' ','_',titulo)
        titulo=respaldo
print(titulo)
descripcion=soup.find_all(id="bookDescriptionBox")
descripcion=re.sub('<p>',' ',str(descripcion))
descripcion=re.sub('</p>',' ',str(descripcion))
descripcion=re.sub('<span>',' ',str(descripcion))
descripcion=re.sub('</span>',' ',str(descripcion))
descripcion=re.sub('</b>',' ',str(descripcion))
descripcion=re.sub('<b>',' ',str(descripcion))
descripcion=re.sub('</div>]',' ',str(descripcion))
respaldo=re.split('>',descripcion)
if re.search('>',descripcion):
    descripcion=respaldo[1]
print(descripcion)
informacionPDF =soup.find_all(style=re.compile("overflow: hidden; zoom: 1;"))
datos=re.sub("<div class=",' ',str(informacionPDF))
datos=re.sub('</div',' ',datos)
datos=re.sub('div',' ',datos)
datos=re.sub('property_label',' ',datos)
datos=re.sub('property_value',' ',datos)
datos=re.sub('<',' ',datos)
datos=re.sub('"',' ',datos)
datos=re.sub('>',' ',datos)
i =re.split('\n',datos,1)
print("\n\n\n\n\n\n")
datos=i[1]
datos=re.sub(']',' ',datos)
if re.search('PDF',datos):
    tipo=re.search('PDF',datos)
    print(tipo.group())
else :
    print("no es PDF")
print(datos)

destinoLibro='/home/dgc7/Documentos/zlibrary/libros1920-1921/'+titulo
fuenteLibro='/home/dgc7/zlibros/libros1920-1921/libro'
if re.sub('\n','',destinoLibro):
    destinoLibro=re.sub('\n','',destinoLibro)
try :
    os.mkdir(destinoLibro)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise    
    print("error al crear la carpeta del libro")
try :
    shutil.move(fuenteLibro,destinoLibro)
except :
   print("error al copiar la carpeda libro")
try :
    os.mkdir(fuenteLibro)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
    print("error al crear la carpeta de descarga de libros")
print("\n\n\n\n\n\n")
txt=open(destinoLibro+'/informacion.txt','w')
try :
    txt.write(titulo+'\n'+ descripcion +'\n'+ datos)
except OSError as e :
    if e.errno != errno.EEXIST:
        raise   

txt2=open(destinoLibro+'/indiseYmas.txt','w')
try :
    txt2.write(str(soup))
except OSError as e :
    if e.errno != errno.EEXIST:
        raise  
    print("error al crear el indise") 

