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
class validarCuentas:
    def __init__(self):
        self.dirNombre='/home/dgc7/ejersiciosLibros/pyaton/ejemplos/scrapin/zlibrari/crearCorreos/nombre.txt'
        self.nombre=open(self.dirNombre,'r+')
        self.email=[]
        for self.d in range(0,101):
            self.email.append(self.nombre.readline()+'asdsdf')
        for self.d in range(0,100):
            self.email[self.d]=re.sub('\n','asdaawderca',self.email[self.d])
            self.email[self.d]=re.sub(
            r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
            normalize( "NFD",self.email[self.d]), 0, re.I
            )
            self.email[self.d]= normalize( 'NFC',self.email[self.d])
  
    def iniciarTor(self,fila):
        self.mailpro=webdriver.Firefox()
        self.mailpro.get('https://maildrop.cc/')
    def ingresarDatos(self,fila):
        self.pulsar=self.mailpro.find_elements_by_xpath('//input')[1]
        self.pulsar.send_keys(self.email[fila])
        self.pulsar.send_keys(Keys.RETURN)
        sleep(6)
        self.correo=self.mailpro.find_elements_by_xpath('//div[@class]')[14]
        self.correo.click()
        sleep(5)
        self.iframe=self.mailpro.find_element_by_tag_name('iframe')
        self.mailpro.switch_to.frame(self.iframe)
        self.html=self.mailpro.page_source
        self.soup=BeautifulSoup(self.html,'html.parser')
        self.urlConfimar = self.soup.find_all('a')[1]
        self.urlM=self.urlConfimar.get('href')
        print(self.urlConfimar.get('href'))
        self.mailpro.get(self.urlM)
    def serrarTor(self):
        self.mailpro.close() 
    def imprimirDatos(self):
        for d in range(0,100):
            print(self.email[d])


for i in range(95,100) :
    sleep(10)
    tor=validarCuentas()
    tor.iniciarTor(1)
    #tor.imprimirDatos()
    sleep(7)
    tor.ingresarDatos(i)
    sleep(10)
    tor.serrarTor()
    print("\n\n\n\n\n\n")
    print(i)
