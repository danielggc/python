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
        self.tbb_dir = "/usr/local/share/tor-browser_en-US"
        self.mailpro = TorBrowserDriver(self.tbb_dir, tbb_logfile_path='test.log')
        self.mailpro.load_url('https://maildrop.cc/')
        
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
        print(self.mailpro.page_source)
        self.mailpro.find_elements_by_xpath('//a[@href]')[1].click()
    def serrarTor(self):
        self.mailpro.close() 
    def imprimirDatos(self):
        for d in range(0,100):
            print(self.email[d])


for i in range(4,8) :
    sleep(10)
    tor=validarCuentas()
    tor.iniciarTor(1)
    tor.imprimirDatos()
    sleep(3)
    tor.ingresarDatos(i)
    sleep(30)
    tor.serrarTor()
