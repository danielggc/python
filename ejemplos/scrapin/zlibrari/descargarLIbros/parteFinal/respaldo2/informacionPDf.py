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
from time import sleep
from bs4 import BeautifulSoup
def contarNueroArchivos():
    fuenteLibro2='/home/dgc7/zlibros/libros1920-1921/libro'
    NumeroDescargas=0
    if os.listdir(fuenteLibro2):
        print(os.listdir(fuenteLibro2))
        for i in os.listdir(fuenteLibro2):
            NumeroDescargas+=1
    return NumeroDescargas

def informaiconPdf(_urlInformacion):
    urlInformacion=_urlInformacion
    archivos=int(contarNueroArchivos())
    print(archivos)
    if archivos==0:
        dirUrlDañadas='/home/dgc7/Documentos/zlibrary/registro/UrlDañadas.txt'
        urlDañadas=open(dirUrlDañadas,'r+')
        for a in urlDañadas.readlines():
            urlDañadas.readline()
        urlDañadas.write(urlInformacion+'\n')
    if archivos!=0:          
        htmlWed=requests.get(urlInformacion)
        soup=BeautifulSoup(htmlWed.content,'html.parser')
        autor=str()
        boleanoAutor=False
        if soup.find_all(itemprop="author")[0]:
            autor=soup.find_all(itemprop="author")[0]
            autor=autor.get('href')
            if re.sub("/g/",'',autor):
                autor=re.sub("/g/",'',autor)
                boleanoAutor=True
                if re.sub("/",'',autor):
                    autor=re.sub("/",'',autor)
        titulo=soup.find_all(class_="moderatorPanelToggler")
        titulo=re.sub('</h1>]',' ',str(titulo))
        respaldo=re.split('>',titulo)
        titulo=respaldo[1]
        if re.split(':',titulo):
            respaldo=re.split(':',titulo)
            titulo=respaldo[0]
            if re.split('\w',titulo):
                try:
                    d=re.search('[A-Z]|[a-z]|[0-9]',titulo,1)
                    print(d.group())
                    respaldo=re.split('[A-Z]|[a-z]|[0-9]',titulo,1)
                    titulo=d.group()+respaldo[1]
                    if re.split('   ',titulo):
                        respaldo=re.split('   ',str(titulo))
                        titulo=respaldo[0]
                    respaldo=re.sub(' ','_',titulo)
                    titulo=respaldo
                except:
                    if boleanoAutor==True:
                        titulo=autor
                    else:
                        dirUrlDañadas='/home/dgc7/Documentos/zlibrary/registro/UrlDañadas.txt'
                        urlDañadas=open(dirUrlDañadas,'r+')
                        for a in urlDañadas.readlines():
                            urlDañadas.readline()
                        urlDañadas.write(urlInformacion+'\n')   
                        os.system('rm -r /home/dgc7/zlibros/libros1920-1921/libro/*.*')     
        print(titulo)
        try:
            descripcion=soup.find_all(id="bookDescriptionBox")
            descripcion=re.sub('<p>',' ',str(descripcion))
            descripcion=re.sub('</p>',' ',str(descripcion))
            descripcion=re.sub('<span>',' ',str(descripcion))
            descripcion=re.sub('</span>',' ',str(descripcion))
            descripcion=re.sub('</b>',' ',str(descripcion))
            descripcion=re.sub('<b>',' ',str(descripcion))
            descripcion=re.sub('</div>]',' ',str(descripcion))
            respaldo=re.split('>',descripcion)
        except:
            print("huvo un error en la direccion de la descripcion")
        try:
            descripcion=respaldo[1]  
        except:
            print("no se encontro la descripcion")
            print(descripcion)
        try:
            informacionPDF =soup.find_all(style=re.compile("overflow: hidden; zoom: 1; margin-top: 30px;"))
            datos=re.sub("<div class=",' ',str(informacionPDF))
            datos=re.sub('</div',' ',datos)
            datos=re.sub('div',' ',datos)
            datos=re.sub('property_label',' ',datos)
            datos=re.sub('property_value',' ',datos)
            datos=re.sub('<',' ',datos)
            datos=re.sub('"',' ',datos)
            datos=re.sub('>',' ',datos)
        except:
            print("huvo un errror en la direccion datos")
        
        try:
            i =re.split('\n',datos,1)
            datos=i[1]
            datos=re.sub(']',' ',datos)
        except:
            print("no se encontraron los datos")
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
        except OSError as e :
            contadorNombreCarpeta=1
            crear=False
            while crear==False:
                try:
                    os.mkdir(destinoLibro+str(contadorNombreCarpeta))
                    crear=True
                except OSError as e :
                    contadorNombreCarpeta+=1             
            shutil.move(fuenteLibro,destinoLibro+str(contadorNombreCarpeta))
            txt=open(destinoLibro+str(contadorNombreCarpeta)+'/informacion.txt','w')
            try :
                if titulo!=autor:
                    if boleanoAutor==True:
                        txt.write(titulo+'\n'+autor+'\n'+ descripcion +'\n'+ datos)
                    else:
                        txt.write(titulo+'\n'+ descripcion +'\n'+ datos)
                else:
                    txt.write(titulo+'\n'+ descripcion +'\n'+ datos)
            except OSError as e :
                if e.errno != errno.EEXIST:
                    raise    
            txt.close()   
            txt=open(destinoLibro+str(contadorNombreCarpeta)+'/indiseYmas.txt','w') 
            try :
                txt.write(str(soup))
            except OSError as e :
                if e.errno != errno.EEXIST:
                    raise      
            txt.close()              
            print("error al copiar la carpeda libro ya esistia")
        try :
            os.mkdir(fuenteLibro)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
            print("error al crear la carpeta de descarga de libros")
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
        

informaiconPdf("https://b-ok.cc/book/5342786/a66251")

