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
        self.contadorCredenciales=0
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
        self.zLibraty.load_url(self.url)
        sleep(4)
        self.html=self.zLibraty.page_source
    def paginaPrinsipal(self,añoInicial,añoFinal):
        self.urlAños='http://zlibraryexau2g3p.onion/s/?yearFrom='+str(añoInicial)+'&yearTo='+str(añoFinal)
        self.url=self.urlAños  
    def cambiarPagina(self,x):
        print("estoy en cambiar pagina prinsipal")
        self.url+='&page='+str(x)
        print(self.url)
    def Crearcsv(self):
        desde=datosDescarga(1)
        asta=datosDescarga(2)
        self.carpetaUrl='/home/dd/Documentos/zlibrary/libros'+str(desde)+'-'+str(asta)+'/url'
        try :
             os.mkdir(self.carpetaUrl)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        self.escrivirUrlWed=csv.writer(open('/home/dd/Documentos/zlibrary/libros'+str(desde)+'-'+str(asta)+'/url/url2.csv','w'))
        self.imprimirUrlPdf=csv.writer(open('/home/dd/Documentos/zlibrary/libros'+str(desde)+'-'+str(asta)+'/url/urlDowload2.csv','w'))
    def credenciales(self,numeroUsuario):
        print("llegue")
        if self.contadorCredenciales==0 or self.contadorCredenciales==20:
            self.zLibraty.load_url("https://singlelogin.org/")
            self.zLibraty.find_element_by_name("redirectToHost").click()
            sleep(3)
            pyautogui.press("down")
            sleep(2)
            pyautogui.press("down")
            sleep(1)
            pyautogui.press("enter")
        sleep(5)
        self.correo=self.usuario[numeroUsuario]
        self.contraseña=self.contraseñaTxT[numeroUsuario]
    def UsuariosYcontraseñas(self):
        self.dir='/home/dd/Documentos/zlibrary/credenciales/contraseñasYcorreos.txt'
        self.data=open(self.dir,'r+')
        for self.i in range(0,200):
            if self.i%2==0 :
                self.usuario.append(self.data.readline())
            if self.i%2!=0:
                self.contraseñaTxT.append(self.data.readline())
    def urlPdf(self,):
        self.contadorCredenciales=1
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
                self.voleano=validarFormato(self.urlpdfGeleneralH)
                guardarNumeroDescargas(self.contadorLibros) 
                print(self.respaldoContador) 
                if self.contadorLibros==self.respaldoContador:
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
                        print("vamos a por el if")
                        sleep(15)
                        if self.voleano==True:
                            self.zLibraty.set_page_load_timeout(12)
                            try:
                                self.zLibraty.load_url(self.urlDowloadPDF)
                            except:
                                sleep(5)
                                self.zLibraty.set_page_load_timeout(7000)
                                print("funciona PDF ")                                
                            self.voleano=False
                            sleep(5)
                            self.contadorLibros+=1
                            self.contadorLibros2+=1
                        else:                          
                            self.zLibraty.set_page_load_timeout(12)
                            try:
                                self.zLibraty.load_url(self.urlDowloadPDF)
                            except:
                                sleep(8)
                                pyautogui.press("down")
                                sleep(2)
                                pyautogui.press("enter")
                            self.zLibraty.set_page_load_timeout(7000)
                            sleep(5)
                            self.contadorLibros+=1
                            self.contadorLibros2+=1
                        self.zLibraty.load_url("about:downloads")
                        self.datosEsperaDescarga()
                        self.peticiones()
                        self.zLibraty.back()
                        informaiconPdf(self.urlpdfGeleneralH)
                        guardarNumeroDescargas(self.contadorLibros)
                self.respaldoContador+=1                   
                if self.contadorLibros==self.respaldoContador:
                    if self.contadorLibros2%10==0:
                        print((self.contadorLibros2-1)%10)
                        self.contador+=1
                        if self.contadorLibros==20:
                            self.contadorCredenciales=20
                            print("saliendo de secion¡¡¡¡¡¡")
                            pyautogui.moveTo(1707,245)
                            pyautogui.hotkey("ctrl","shift","u")
                            sleep(2)
                            pyautogui.press("enter")
                            sleep(7)
                            pyautogui.press("enter")
                            sleep(15)
                        else:
                            print("saliendo de secion")
                            self.zLibraty.get("http://zlibraryexau2g3p.onion/logout.php")          
                        self.contadorUsuarios+=1
                        print(self.contadorUsuarios)
                        try:
                            self.zLibraty.switch_to_window(self.zLibraty.window_handles[0])
                        except:
                            print("error al cambian de  ventana")
                       
                        usuarioUsadosReescrivir(self.contadorUsuarios)
                        print("por aqui¿¿¿¿¿¿")
                        self.credenciales(self.contadorUsuarios)
                        self.contadorCredenciales=1
                        print("no por aqui¿¿¿¿¿¿")
                        sleep(20)
                        self.iniciarSecion()
                        sleep(15)
                        self.paginaDescargas()
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
            archivos=int(contarNueroArchivos())
            print(archivos)
            self.zLibraty.load_url("about:downloads")
            self.datosEsperaDescarga()
            self.peticiones()
            self.zLibraty.back()
            informaiconPdf(self.urlpdfGeleneralH)
    def DescargarContenido(self,_html):         
        self.contenido=_html
    def serrarTor(self):
         self.zLibraty.close()
    def datosEsperaDescarga(self):
        sleep(4)
        self.htmlValidador=self.zLibraty.page_source
    def validarDescarga(self):
        self.htmlFalce=self.zLibraty.page_source
        self.soupFalce=BeautifulSoup(self.htmlFalce,"html.parser")
        self.validarfalce=self.soupFalce.find_all("description",class_="downloadDetails downloadDetailsNormal")
        self.respuestafalce=re.search("value=.+",str(self.validarfalce))
        self.buscarFalse=self.respuestafalce.group()
        if re.search("Canceled",self.buscarFalse):
            print("se daño al descarga =(")
            sleep(5)
            pyautogui.click(1393,139)
            sleep(5)
        else :
            if re.search("Failed",self.buscarFalse):
                print("se daño al descarga pero vamos a solucionarlo =( ")
                sleep(5)
                pyautogui.click(1393,139)
                sleep(5)
            else:    
                print("la descarga va bien =)")
    def peticiones(self):   
        self.validarDescarga()      
        self.carga=0
        self.daño=0
        self.conteo=0
        while self.carga<100:
            self.soup=BeautifulSoup(self.htmlValidador,"html.parser")
            try:
                self.archivoDescarga=self.soup.find_all("progress",class_="downloadProgress")
                self.respaldo=re.split("value",str(self.archivoDescarga))
                self.tiempo=re.search("[0-9]+",self.respaldo[1])
                print(self.tiempo.group())
                self.carga=int(self.tiempo.group())
                self.datosEsperaDescarga()
                sleep(3)
                self.validarDescarga()
                if self.conteo==3:
                    pyautogui.press("enter")
                    self.conteo=0
            except:
                print("o  no ,se daño la descargar y no la e podido volver a iniciar")
                if self.daño==7:
                    os.system('rm -r /home/dd/zlibros/libros1920-1921/libro/*.*')         
                    raise
                self.daño+=1
                sleep(5)




def contarNueroArchivos():
    fuenteLibro='/home/dd/zlibros/libros1920-1921/libro'
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
        dirUrlDañadas='/home/dd/Documentos/zlibrary/registro/UrlDañadas.txt'
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
        if re.split('[A-Z]|[a-z]|[0-9]',titulo):
            print(titulo)
            try:
                d=re.search('[A-Z]|[a-z]|[0-9]|\w',titulo,1)
                print(d.group())
                respaldo=re.split('[A-Z]|[a-z]|[0-9]|\w',titulo,1)
                titulo=d.group()+respaldo[1]
                if re.split('   ',titulo):
                    respaldo=re.split('   ',str(titulo))
                    titulo=respaldo[0]
                respaldo=re.sub(' ','_',titulo)
                titulo=respaldo
                if re.search("/","_",titulo):
                    titulo=re.sub("/","_",titulo)
                if re.search("'\'","_",titulo):
                    titulo=re.sub("/","_",titulo)
                    print("ey aqui hay un bacaeslach si es que aparesio un problema")
            except:
                if boleanoAutor==True:
                    titulo=autor
                else:
                    dirUrlDañadas='/home/dd/Documentos/zlibrary/registro/UrlDañadas.txt'
                    urlDañadas=open(dirUrlDañadas,'r+')
                    for a in urlDañadas.readlines():
                        urlDañadas.readline()
                    urlDañadas.write(urlInformacion+'\n')   
                    os.system('rm -r /home/dd/zlibros/libros1920-1921/libro/*.*')     
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
        desde=datosDescarga(1)
        asta=datosDescarga(2)
        destinoLibro='/home/dd/Documentos/zlibrary/libros'+str(desde)+'-'+str(asta)+'/'+str(titulo)
        print(destinoLibro)
        fuenteLibro='/home/dd/zlibros/libros1920-1921/libro'
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
                        txt.write(titulo+'\n'+autor+'\n'+ descripcion +'\n'+ datos+"\n"+urlInformacion)
                    else:
                        txt.write(titulo+'\n'+ descripcion +'\n'+ datos+"\n"+urlInformacion)
                else:
                    txt.write(titulo+'\n'+ descripcion +'\n'+ datos+"\n"+urlInformacion)
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
            txt.write(titulo+'\n'+ descripcion +'\n'+ datos+"\n"+urlInformacion)
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
    else:
        dirUrlDañadas='/home/dd/Documentos/zlibrary/registro/UrlDañadas.txt'
        urlDañadas=open(dirUrlDañadas,'r+')
        for a in urlDañadas.readlines():
            urlDañadas.readline()
        urlDañadas.write(urlInformacion+'\n')   
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
    fuenteLibro='/home/dd/zlibros/libros1920-1921/libro'
    descargado=False
    numeroArchivo=contarNueroArchivos()
    print("esperando la descarga ...")
    while numeroArchivo >1:
        numeroArchivo=contarNueroArchivos()
        sleep(4)
        pyautogui.press("enter")
    sleep(2)
    archivos= os.listdir(fuenteLibro)
    print(archivos)
    while descargado==False:
        if re.search('Sin|sin',str(archivos)):
            if re.search('confirmar|Confirmar',str(archivos)):
                pyautogui.press("enter")
                sleep(4)
            else:
                descargado=True
        else:
            if re.search('Unconfirmed|unconfirmed',str(archivos)):
                pyautogui.press("enter")
                sleep(4)
            else:
                descargado=True
        archivos=os.listdir(fuenteLibro)
    print("termine",archivos)


def guardarNumeroDescargas(_numeroDescargas):
    dirRegistroDescargas='/home/dd/Documentos/zlibrary/registro/registroDescargas.txt'
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
    dirRegistroDescargas='/home/dd/Documentos/zlibrary/registro/registroDescargas.txt'
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
    dirRegistroDescargas='/home/dd/Documentos/zlibrary/registro/registroDescargas.txt'
    datoAños=open(dirRegistroDescargas,'r')
    contador=0
    for i in datoAños.readlines():
        contador+=1
        if indicador==contador:
            dato=i
            print("datos=)=)=)=)",dato)
    datoAños.close()
  
    return int(dato)



def usuarioUsadosLeer():
    dirRegistroDescargas='/home/dd/Documentos/zlibrary/registro/registroUsuario.txt'
    datosAñosU=open(dirRegistroDescargas,'r')
    datosUsuarios=int(datosAñosU.readline())
    return datosUsuarios


def usuarioUsadosReescrivir(_usuariUsados):
    usuariUsados =_usuariUsados
    dirRegistroDescargas='/home/dd/Documentos/zlibrary/registro/registroUsuario.txt'
    datosAñosU=open(dirRegistroDescargas,'w+')
    datosAñosU.write(str(usuariUsados))



    

añoX=datosDescarga(1)
añoY=datosDescarga(2)
conteoPagina=datosDescarga(3)
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
    wedPrinsipal.paginaPrinsipal(añoX,añoY)
    carpetalibrosAños='/home/dd/Documentos/zlibrary/libros'+str(añoX)+'-'+str(añoY)
    try :
        os.mkdir(carpetalibrosAños)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise    
        print("error al crear la carpeta del libro")
    try:
        while conteoPagina <11:
            guardarHistorial(añoX,añoY,conteoPagina)
            print(conteoPagina)
            print('hola')
            print(conteoPagina)
            print("holas ya terminaste una pagina ?")
            wedPrinsipal.cambiarPagina(conteoPagina)            
            wedPrinsipal.paginaDescargas()
            sleep(6)
            wedPrinsipal.urlPdf()
            print(conteoPagina)
            print('hola')
            guardarNumeroDescargas(0)
            conteoPagina+=1
            print(conteoPagina)
            guardarHistorial(añoX,añoY,conteoPagina)
    except OSError as a :
        print("no es so eso ======u")
        print(a.strerror)
        guardarHistorial(añoX,añoY,conteoPagina)
   
    conteoPagina=1
    añoY+=2
    añoX+=2
    print("vamos a cambiar de año ¡¡¡¡¡ yupy")
    print(añoX,añoY)
    guardarHistorial(añoX,añoY,conteoPagina)
    sleep(30)


