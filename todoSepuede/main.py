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
import pyautogui
# trampas http://dl39.zlibcdn.com/dtoken/ee9a8e4f62ed4dbdb5c39eb772c3c300   ?
#https://singlelogin.org/?logoutAll
#https://b-ok.cc/book/
class DescargarPdf:
    def __init__(self):
        self.url='https://www.bibliadelprogramador.com/search/label/Manuales?updated-max=2013-08-13T23%3A13%3A00-03%3A00&max-results=14#PageNo=9' 
    def iniciarTor(self):
        self.zLibraty=webdriver.Firefox()
    def paginaPrinsipal(self):
        self.zLibraty.get(self.url)
        sleep(7)
        self.html=self.zLibraty.page_source
    def urlPdf(self):
        self.html=requests.get(self.url)
        self.boleanoPdf=0
        self.respaldoContador=0
        self.soup=BeautifulSoup(self.html.content,'html.parser')
        for self.urlwed in self.soup.find_all(class_="post-title entry-title") :
            self.contador=0
            self.urlwed=self.urlwed.find('a',href=re.compile(''))
            self.urlDowload=self.urlwed.get('href')
            print(self.urlDowload)
            self.zLibraty.get(self.urlDowload)
            sleep(10)
            self.descargar=self.zLibraty.find_elements_by_xpath('//div[@class="post-body entry-content"]//a[@href]')[1]
            self.descargar.click()
            sleep(7)
            pyautogui.moveTo(1707,245,1)
            pyautogui.press("enter")
            sleep(5)

    def serrarTor(self):
         self.zLibraty.close()







wedPrinsipal=DescargarPdf()
sleep(5)
wedPrinsipal.iniciarTor()
wedPrinsipal.urlPdf()
  
