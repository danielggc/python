
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.utils import keys_to_typing
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

from tbselenium.tbdriver import TorBrowserDriver
import tbselenium.common as cm
from tbselenium.utils import launch_tbb_tor_with_stem
from selenium.webdriver.common.keys import Keys
from time import sleep
from tbselenium.utils import launch_tbb_tor_with_stem
from selenium.webdriver.common.by import By
from argparse import ArgumentParser
#https://singlelogin.org/?logoutAll
#https://b-ok.cc/book/
class DescargarPdf:
    def __init__(self):
        self.tbb_dir = "/usr/local/share/tor-browser_en-US"
        self.usuario=[]
        self.contraseñaTxT=[]
        self.conversor='?convertedTo=pdf'
    def iniciarTor(self):
        self.zLibraty = TorBrowserDriver(self.tbb_dir, tbb_logfile_path='test.log')
    def iniciarSecion(self):
        self.zLibraty.refresh()
        sleep(10)
        self.element=self.zLibraty.find_element_by_name("email")
        self.element.send_keys(self.correo)
        sleep(2)
        self.element2=self.zLibraty.find_elements_by_class_name("form-control")[1]
        self.element2.send_keys(self.contraseña)
        self.element2.send_keys(Keys.RETURN)
    def paginaDescargas(self):
        self.zLibraty.load_url(self.url)
        self.html=self.zLibraty.page_source
    def paginaPrinsipal(self,añoInicial,añoFinal):
        self.urlAños='http://zlibraryexau2g3p.onion/s/?yearFrom='+str(añoInicial)+'&yearTo='+str(añoFinal)
        self.url=self.urlAños  
    def cambiarPagina(self,x):
        self.url+='&page='+str(x)
    def Crearcsv(self):
        print("hola")
        self.carpetaUrl='/home/dgc7/Documentos/zlibrary/libros1920-1921/url'
        try :
             os.mkdir(self.carpetaUrl)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        self.escrivirUrlWed=csv.writer(open('/home/dgc7/Documentos/zlibrary/libros1920-1921/url/url2.csv','w'))
        self.imprimirUrlPdf=csv.writer(open('/home/dgc7/Documentos/zlibrary/libros1920-1921/url/urlDowload2.csv','w'))
    def credenciales(self,numeroUsuario):
        self.correo=self.usuario[numeroUsuario]
        self.contraseña=self.contraseñaTxT[numeroUsuario]
        self.urlLoguin='http://zlibraryexau2g3p.onion'
        self.zLibraty.load_url(self.urlLoguin)
    def UsuariosYcontraseñas(self):
        self.dir='/home/dgc7/ejersiciosLibros/pyaton/ejemplos/scrapin/zlibrari/descargarLIbros/descargarparte1/contraseñasYcorreos.txt'
        self.data=open(self.dir,'r+')
        for self.i in range(0,200):
            if self.i%2==0 :
                self.usuario.append(self.data.readline())
            if self.i%2!=0:
                self.contraseñaTxT.append(self.data.readline())
    def urlPdf(self,contador,_contadorusuarios):
        self.boleanoPdf=0
        self.contadorUsuariosCon=_contadorusuarios
        self.contadorLibros2=0
        self.contadorLibros=0
        self.Crearcsv()
        self.soup=BeautifulSoup(self.html,'html.parser')
        for self.urlwed in self.soup.find_all(itemprop = "name") :
            self.contador=0
            self.urlwed=self.urlwed.find('a',href=re.compile(''))
            self.urlDowload=self.urlwed.get('href')
            self.urlpdfGeleneralH=re.sub('/book/','https://b-ok.cc/book/',self.urlDowload)
            self.urlDowload=re.sub('/book/','http://zlibraryexau2g3p.onion/book/',self.urlDowload)
            self.escrivirUrlWed.writerow([self.urlDowload])
            print(self.urlDowload)
            self.contadorLibros+=1
            self.contadorLibros2+=1
            if self.contadorLibros2==10:
                self.contador+=1
                self.serrarTor()
                sleep(4)
                self.iniciarTor()
                self.contadorUsuariosCon+=1
                print(self.contadorUsuariosCon)
                self.credenciales(contadorusuarios)
                self.iniciarSecion()
                sleep(7)
                self.contadorLibros2=0
                sleep(15)
                if self.contador==5:
                    self.contador=0
            voleano=validarFormato(self.urlpdfGeleneralH)                        
            for self.urlRedirec in range(0,1):
                self.zLibraty.load_url(self.urlDowload)
                sleep(5)
                self.htmlPdf=self.zLibraty.page_source
                self.soupRedirec=BeautifulSoup(self.htmlPdf,'html.parser')
                self.urlDowloadPDF=self.soupRedirec.find(class_="btn btn-primary dlButton addDownloadedBook")
                self.urlDowloadPDF=self.urlDowloadPDF.get('href')
                self.urlDowloadPDF=re.sub('/dl/','http://zlibraryexau2g3p.onion/dl/',self.urlDowloadPDF)
                self.imprimirUrlPdf.writerow([self.urlDowloadPDF])
                print(self.urlDowloadPDF)
                if voleano==True:
                    self.zLibraty.get(self.urlDowloadPDF)
                    voleano=False
                else:
                    self.convertirpdf=str(self.urlDowloadPDF)+str(self.conversor)
                    self.zLibraty.get(self.convertirpdf)
                sleep(20)
                tiempoDescarga()
                informaiconPDf(self.urlpdfGeleneralH)
    def DescargarContenido(self,_html):         
        self.contenido=_html
    def serrarTor(self):
         self.zLibraty.close()

def informaiconPDf(_urlInformacion):
    urlInformacion=_urlInformacion
    htmlWed=requests.get(urlInformacion)
    soup=BeautifulSoup(htmlWed.content,'html.parser')
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
    except :
        print("error al copiar la carpeda libro")
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
   
def validarFormato(_url):
    formatoPdf=True
    url=_url
    htmlFormato=requests.get(url)
    soup=BeautifulSoup(htmlFormato.content,'html.parser')
    informacionPDF =soup.find_all(style=re.compile("overflow: hidden; zoom: 1;"))
    datos=re.sub("<div class=",' ',str(informacionPDF))
    datos=re.sub('</div',' ',datos)
    datos=re.sub('div',' ',datos)
    if re.search('PDF',datos):
        formatoPdf=True  
    else :
        formatoPdf=False
    return formatoPdf


def tiempoDescarga():
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


wedPrinsipal=DescargarPdf()
wedPrinsipal.iniciarTor()
wedPrinsipal.UsuariosYcontraseñas()
sleep(7)
wedPrinsipal.credenciales(0)
sleep(7)
wedPrinsipal.iniciarSecion()
sleep(10)
contadorPaginas=2
contadorusuarios=0
añosX=1920
añoY=1921
for i in range(0,3):
    wedPrinsipal.paginaPrinsipal(añosX+i,añoY+i)
    for f in range(1,10):
        wedPrinsipal.cambiarPagina(f)            
        wedPrinsipal.paginaDescargas()
        sleep(6)
        wedPrinsipal.urlPdf(contadorPaginas,contadorusuarios)
    sleep(40)
