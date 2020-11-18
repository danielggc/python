import unittest
from tbselenium.tbdriver import TorBrowserDriver
import tbselenium.common as cm
from tbselenium.utils import launch_tbb_tor_with_stem
from selenium.webdriver.common.keys import Keys
from time import sleep
from tbselenium.utils import launch_tbb_tor_with_stem
from selenium.webdriver.common.by import By
from argparse import ArgumentParser
import re
import random
from unicodedata import normalize
import csv


dirNombre='home/dgc7/ejersiciosLibros/pyaton/ejemplos/scrapin/zlibrari/crearCorreos'
class crearCorros:
    def __init__(self):
        self.urlProtocoe ='http://3g2upl4pq6kufc4m.onion','https://mail.protonmail.com/create/new','https://singlelogin.org/registration.php'
        print(self.urlProtocoe[2])
        self.tbb_dir = "/usr/local/share/tor-browser_en-US"
        self.protocoe = TorBrowserDriver(self.tbb_dir, tbb_logfile_path='test.log')
        self.dirNombre='/home/dgc7/ejersiciosLibros/pyaton/ejemplos/scrapin/zlibrari/crearCorreos/nombre.txt'
        self.nombre=open(self.dirNombre,'r+')
        self.dirapellido='/home/dgc7/ejersiciosLibros/pyaton/ejemplos/scrapin/zlibrari/crearCorreos/apellidos.txt'
        self.apellido=open(self.dirapellido,'r+')
        self.dirContrasenna='/home/dgc7/ejersiciosLibros/pyaton/ejemplos/scrapin/zlibrari/crearCorreos/contraseña.txt'
        self.contrasenna=open(self.dirContrasenna,'r+')
        self.dirCotrasenna2='/home/dgc7/ejersiciosLibros/pyaton/ejemplos/scrapin/zlibrari/crearCorreos/contraseña2.txt'
        self.Contrasenna2=open(self.dirCotrasenna2,'r+')
        self.datosContrasenna=[]
        self.lista=[]
        for self.d in range(0,101):
            self.lista.append(self.nombre.readline()+'asdsdf')
            self.datosContrasenna.append(self.contrasenna.readline()+"blabal")
        for self.d in range(0,100):
            self.lista[self.d]=re.sub('\n','asdaawderca',self.lista[self.d])
            self.datosContrasenna[self.d]=re.sub('\n','radabanals',self.datosContrasenna[self.d])
            self.lista[self.d]=re.sub(
            r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
            normalize( "NFD",self.lista[self.d]), 0, re.I
            )
            self.lista[self.d]= normalize( 'NFC',self.lista[self.d])
            self.datosContrasenna[self.d]=re.sub(
            r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
            normalize( "NFD",self.datosContrasenna[self.d]), 0, re.I
             )
            self.datosContrasenna[self.d]= normalize( 'NFC',self.datosContrasenna[self.d])
            self.lista[self.d]+='@maildrop.cc'
    def iniciarTor(self):
        self.protocoe.load_url(self.urlProtocoe[2])
    def ingresarDatos(self,fila):
        self.eamil=self.protocoe.find_element_by_name('email')
        self.eamil.click()
        sleep(random.uniform(1.0,4))
        self.eamil.send_keys(self.lista[fila])
        self.pasword=self.protocoe.find_element_by_name("password")
        self.pasword.click()
        sleep(random.uniform(1.0,5))
        self.pasword.send_keys(self.datosContrasenna[fila])
        self.name=self.protocoe.find_element_by_name("name")
        sleep(random.uniform(1.0,6))
        self.name.click()
        self.name.send_keys(self.datosContrasenna[fila])
        sleep(random.uniform(2.0,8.7))
        self.name.send_keys(Keys.RETURN)
    def serrarTor(self):
        self.protocoe.close() 
    def imprimirDatos(self):
        #self.dirscv='/home/dgc7/ejersiciosLibros/pyaton/ejemplos/scrapin/zlibrari/emailFalsos/contraseñasYcorreos.csv'
        #self.datos=csv.writer(open(self.dirscv,'w'))
        for d in range(0,100):
            #self.datos.writerow([self.lista[d]])
            #self.datos.writerow([self.datosContrasenna[d]])
            print(self.lista[d])
            print(self.datosContrasenna[d])


for a  in range(91,100):
    tor=crearCorros()
    tor.iniciarTor()
    sleep(30)
    tor.ingresarDatos(a)
    sleep(30)
    tor.imprimirDatos()
    sleep(random.uniform(30.0,50))
    tor.serrarTor()
    print('\n\n\n\n\n\n\n\n')
    print(a)


