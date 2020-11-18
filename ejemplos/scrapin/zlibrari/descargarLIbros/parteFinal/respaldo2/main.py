
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.utils import keys_to_typing
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
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
from selenium.webdriver.support.ui import WebDriverWait
from tbselenium.tbdriver import TorBrowserDriver
import tbselenium.common as cm
from tbselenium.utils import launch_tbb_tor_with_stem
from selenium.webdriver.common.keys import Keys
from time import sleep
from tbselenium.utils import launch_tbb_tor_with_stem
from selenium.webdriver.common.by import By
from argparse import ArgumentParser
# trampas http://dl39.zlibcdn.com/dtoken/ee9a8e4f62ed4dbdb5c39eb772c3c300   ?
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
        self.element=self.zLibraty.find_element_by_name("email")
        self.element.send_keys(self.correo)
        sleep(2)
        self.element2=self.zLibraty.find_elements_by_class_name("form-control")[1]
        self.element2.send_keys(self.contraseña)
        self.element2.send_keys(Keys.RETURN)
    def paginaDescargas(self):
        print("estoy en la funcion paginaDescagas")
        sleep(4)
        self.zLibraty.get(self.url)
        self.html=self.zLibraty.page_source
    def paginaPrinsipal(self,añoInicial,añoFinal):
        self.urlAños='http://zlibraryexau2g3p.onion/s/?yearFrom='+str(añoInicial)+'&yearTo='+str(añoFinal)
        self.url=self.urlAños  
    def cambiarPagina(self,x):
        self.url+='&page='+str(x)
    def Crearcsv(self):
        self.carpetaUrl='/home/dgc7/Documentos/zlibrary/libros1920-1921/url'
        try :
             os.mkdir(self.carpetaUrl)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        self.escrivirUrlWed=csv.writer(open('/home/dgc7/Documentos/zlibrary/libros1920-1921/url/url2.csv','w'))
        self.imprimirUrlPdf=csv.writer(open('/home/dgc7/Documentos/zlibrary/libros1920-1921/url/urlDowload2.csv','w'))
    def credenciales(self,numeroUsuario):
        print("llegue")
        self.correo=self.usuario[numeroUsuario]
        self.contraseña=self.contraseñaTxT[numeroUsuario]
        self.urlLoguin='http://zlibraryexau2g3p.onion'
        self.zLibraty.get(self.urlLoguin)
    def UsuariosYcontraseñas(self):
        self.dir='/home/dgc7/Documentos/zlibrary/credenciales/contraseñasYcorreos.txt'
        self.data=open(self.dir,'r+')
        for self.i in range(0,200):
            if self.i%2==0 :
                self.usuario.append(self.data.readline())
            if self.i%2!=0:
                self.contraseñaTxT.append(self.data.readline())
    def urlPdf(self,):
        self.boleanoPdf=0
        self.respaldoContador=0
        self.contadorUsuarios=usuarioUsadosLeer()
        self.contadorLibros=datosDescarga(4)
        self.contadorLibros2=self.contadorLibros%10
        self.Crearcsv()
        self.soup=BeautifulSoup(self.html,'html.parser')
        try:
            for self.urlwed in self.soup.find_all(itemprop = "name") :
                self.contador=0
                self.urlwed=self.urlwed.find('a',href=re.compile(''))
                self.urlDowload=self.urlwed.get('href')
                self.urlpdfGeleneralH=re.sub('/book/','https://b-ok.cc/book/',self.urlDowload)
                self.urlDowload=re.sub('/book/','http://zlibraryexau2g3p.onion/book/',self.urlDowload)
                self.escrivirUrlWed.writerow([self.urlDowload])
                print(self.urlDowload)
                voleano=validarFormato(self.urlpdfGeleneralH)
                guardarNumeroDescargas(self.contadorLibros) 
                print(self.respaldoContador) 
                if self.contadorLibros==self.respaldoContador:
                    for self.urlRedirec in range(0,1):
                        self.zLibraty.get(self.urlDowload)
                        sleep(5)
                        self.htmlPdf=self.zLibraty.page_source
                        self.soupRedirec=BeautifulSoup(self.htmlPdf,'html.parser')
                        self.urlDowloadPDF=self.soupRedirec.find(class_="btn btn-primary dlButton addDownloadedBook")
                        self.urlDowloadPDF=self.urlDowloadPDF.get('href')
                        self.urlDowloadPDF=re.sub('/dl/','http://zlibraryexau2g3p.onion/dl/',self.urlDowloadPDF)
                        self.imprimirUrlPdf.writerow([self.urlDowloadPDF])
                        print(self.urlDowloadPDF)
                        print("vamos a por el if")
                        sleep(10)
                        if voleano==True:
                            self.zLibraty.set_page_load_timeout(8)
                            try:
                               self.zLibraty.get(self.urlDowloadPDF)
                            except:
                                self.zLibraty.set_page_load_timeout(70)
                                self.zLibraty.refresh()
                                print("funciona PDF ")
                                
                            voleano=False
                            sleep(5)
                            self.contadorLibros+=1
                            self.contadorLibros2+=1
                        else:                          
                            try:
                                self.zLibraty.set_page_load_timeout(5)
                                try:
                                    self.zLibraty.get(self.urlDowloadPDF)
                                except:
                                    sleep(4)
                                    pyautogui.press("down")
                                    sleep(2)
                                    pyautogui.press("enter")
                                self.zLibraty.set_page_load_timeout(70)
                            except:
                                print("\nerror al controlasr el teclado y dar enter\n")
                                raise
                            sleep(5)
                            self.zLibraty.refresh()
                            self.contadorLibros+=1
                            self.contadorLibros2+=1
                        sleep(20)
                        tiempoDescarga()
                        informaiconPdf(self.urlpdfGeleneralH)
                self.respaldoContador+=1                   
                if self.contadorLibros==self.respaldoContador:
                    if self.contadorLibros2%10==0:
                        print((self.contadorLibros2-1)%10)
                        self.contador+=1
                        pyautogui.hotkey("ctrl","shift","u")
                        sleep(2)
                        pyautogui.press("enter")
                        sleep(7)
                        pyautogui.press("enter")
                        sleep(15)
                        self.contadorUsuarios+=1
                        print(self.contadorUsuarios)
                        try:
                            self.zLibraty.switch_to_window(self.zLibraty.window_handles[0])
                        except:
                            print("error al cambian de  ventana")
                        usuarioUsadosReescrivir(self.contadorUsuarios)
                        print("por aqui¿¿¿¿¿¿")
                        self.credenciales(self.contadorUsuarios)
                        print("no por aqui¿¿¿¿¿¿")
                        sleep(23)
                        self.iniciarSecion()
                        sleep(7)
                        self.contadorLibros2=0
                        sleep(15)
                        print("numero de li bros por usuario ",self.contadorLibros2)
                        if self.contador==5:
                            self.contador=0                 
        except OSError as e :
            print(e.strerror)
            print("error en la urlPdf:::::")
            guardarNumeroDescargas(self.contadorLibros)
            usuarioUsadosReescrivir(self.contadorUsuarios)
            print(self.contadorLibros)
            raise
        print("termine la pagina")
    def DescargarContenido(self,_html):         
        self.contenido=_html
    def serrarTor(self):
         self.zLibraty.close()




def contarNueroArchivos():
    fuenteLibro='/home/dgc7/zlibros/libros1920-1921/libro'
    NumeroDescargas=0
    if os.listdir(fuenteLibro):
        for i in os.listdir(fuenteLibro):
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
                print("*")
                sleep(0.1)
            else:
                descargado=True
        else:
            if re.search('Unconfirmed|unconfirmed',str(archivos)):
                print("*")
                sleep(0.1)
            else:
                descargado=True
        archivos=os.listdir(fuenteLibro)
    print("termine",archivos)


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
            print(datos)
    lista.append(nuemroDescargas)
    datoAñosF.close()
    datoAñosF=open(dirRegistroDescargas,'w')
    datoAñosF.close()
    datoAñosF=open(dirRegistroDescargas,'r+')
    for a in range(0,4):
        datoAñosF.write(str(lista[a])+'\n')




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


def usuarioUsadosReescrivir(_usuariUsados):
    usuariUsados =_usuariUsados
    dirRegistroDescargas='/home/dgc7/Documentos/zlibrary/registro/registroUsuario.txt'
    datosAñosU=open(dirRegistroDescargas,'w+')
    datosAñosU.write(str(usuariUsados))

wedPrinsipal=DescargarPdf()
wedPrinsipal.iniciarTor()
sleep(15)
wedPrinsipal.UsuariosYcontraseñas()
sleep(15)
wedPrinsipal.credenciales(usuarioUsadosLeer())
sleep(7)
wedPrinsipal.iniciarSecion()
sleep(10)
for i in range(0,3):
    añoX=datosDescarga(1)
    añoY=datosDescarga(2)
    conteoPagina=datosDescarga(3)
    wedPrinsipal.paginaPrinsipal(añoX,añoY)
    try:
        for conteoPagina in range(conteoPagina,10):
            print("holas ya terminaste una pagina ?")
            wedPrinsipal.cambiarPagina(conteoPagina)            
            wedPrinsipal.paginaDescargas()
            sleep(6)
            wedPrinsipal.urlPdf()
            guardarHistorial(añoX,añoY,conteoPagina)
            guardarNumeroDescargas(0)
    except OSError as a :
        print("no es so eso ======u")
        print(a.strerror)
        guardarHistorial(añoX,añoY,conteoPagina)
    guardarHistorial(añoX,añoY,conteoPagina)
    sleep(30)

