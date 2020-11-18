from time import sleep
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.utils import keys_to_typing
from selenium.webdriver.common.keys import Keys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class buscadorGoogle:
    
    def __init__(self,url_):
        self.correo='danielgrecia7@gmail.com'
        self.contraseña='ddggcc77'
        self.url=url_
    def llamarGoogle(self):
        self.google=webdriver.Firefox()  
        self.google.get(self.url)
        self.element=self.google.find_element_by_name("q")
        self.element.click()
        sleep(2)
        sleep(120)
        self.element.send_keys("python")
        self.element.send_keys(Keys.RETURN)
        self.google.get('https://b-ok.cc/book/1240102/21cd11')
        sleep(120)
        self.google.get('https://b-ok.cc/dl/841322/855eff')
       
        sleep(120)
    def cerraPestaña(self):
        self.google.close()
    def urlAtual(self):
        return self.google.current_url

_url='https://www.google.es/'
google=buscadorGoogle(_url)
google.llamarGoogle()
#danielgrecia7@gmail.com