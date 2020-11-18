import requests
import csv
import re
import wget
import shutil
import os
import errno
from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import sleep
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.utils import keys_to_typing
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import re
import random
from unicodedata import normalize

profile=webdriver.FirefoxProfile('/home/dgc7/.mozilla/firefox/7aebrp31.dd7')
profile.set_preference("browser.download.panel.shown", False)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk","application/zip")
profile.set_preference('browser.download.folderList',2)
profile.set_preference('browser.download.dir','/home/dgc7/zlibros/libros1920-1921')

      
dirNombre='home/dgc7/ejersiciosLibros/pyaton/ejemplos/scrapin/zlibrari/crearCorreos'
class crearCorros:
    def __init__(self):
        self.urlProtocoe ='http://3g2upl4pq6kufc4m.onion','https://mail.protonmail.com/create/new'
        print(self.urlProtocoe[1])
        self.proxies={
        "http":"http://188.165.16.230:3129",
        "https":"https://188.165.16.230:3129",
        }       
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
            self.datosContrasenna.append(self.contrasenna.readline()+self.Contrasenna2.readline())
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
    def iniciarTor(self):
        self.protocoe=webdriver.Firefox(profile)
        self.protocoe.get(self.urlProtocoe[1])
    def ingresarDatos(self,fila):
        self.pasword=self.protocoe.find_element_by_name("password")
        self.pasword.click()
        sleep(random.uniform(1.0,4))
        self.pasword.send_keys(self.datosContrasenna[fila])
        self.pasword=self.protocoe.find_element_by_name("passwordc")
        sleep(random.uniform(1.0,3))
        self.pasword.click()
        self.pasword.send_keys(self.datosContrasenna[fila])
        sleep(random.uniform(2.0,5.7))
        self.iframes=self.protocoe.find_element_by_tag_name("iframe")
        self.protocoe.switch_to.frame(self.iframes)
        self.usuario=self.protocoe.find_element_by_xpath('//input')
        self.usuario.click()
        self.usuario.send_keys(self.lista[fila])
        sleep(random.uniform(0,5))
        self.usuario.send_keys(Keys.ENTER)
        self.protocoe.switch_to.default_content()
        sleep(20)
        self.enter=self.protocoe.find_element_by_xpath('//button[@class="pm_button primary modal-footer-button"]')
        self.enter.click()
    def serrarTor(self):
        self.protocoe.close() 
    def imprimirDatos(self):
        for d in range(0,100):
            print(self.lista[d])
            #print(self.datosContrasenna[d])
        
tor=crearCorros()
tor.iniciarTor()
sleep(30)
tor.ingresarDatos(13)
sleep(30)
tor.imprimirDatos()
#https://mail.protonmail.com/create/new?language=es
#passwordc
#password
#asdsdfdashgf1233423
#3 4 10 11 12 13