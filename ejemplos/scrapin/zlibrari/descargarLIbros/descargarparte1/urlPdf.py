
from urllib.request import urlopen
from bs4 import BeautifulSoup
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


class DescargarPdf:
    def __init__(self):
        self.tbb_dir = "/usr/local/share/tor-browser_en-US"
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
        self.zLibraty.load_url(self.url)
        self.html=self.zLibraty.page_source
    def paginaPrinsipal(self,añoInicial,añoFinal):
        self.urlAños='https://b-ok.cc/s/?yearFrom='+str(añoInicial)+'&yearTo='+str(añoFinal)
        self.url=self.urlAños
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
    def credenciales(self):
        self.correo='danielgrecia7@gmail.com'
        self.contraseña='ddggcc77'
        self.urlLoguin='https://singlelogin.org/?logoutAll'
        self.zLibraty.load_url(self.urlLoguin)
    def urlPdf(self):
        self.Crearcsv()
        self.soup=BeautifulSoup(self.html,'html.parser')
        for self.urlwed in self.soup.find_all(itemprop = "name") :
            self.urlwed=self.urlwed.find('a',href=re.compile(''))
            self.urlDowload=self.urlwed.get('href')
            self.urlDowload=re.sub('/book/','https://b-ok.cc/book/',self.urlDowload)
            self.escrivirUrlWed.writerow([self.urlDowload])
            print(self.urlDowload)


wedPrinsipal=DescargarPdf()
wedPrinsipal.iniciarTor()
sleep(3)
wedPrinsipal.credenciales()
sleep(2)
wedPrinsipal.iniciarSecion()
sleep(7)
wedPrinsipal.paginaPrinsipal(1922,1923)

    
