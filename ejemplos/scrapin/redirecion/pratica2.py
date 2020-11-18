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
        self.url=url_
        self.correo='danielgrecia7@gmail.com'
        self.contraseña='ddggcc77'
    def llamarGoogle(self):
        self.google=webdriver.Firefox()  
        self.google.get(self.url)
        #self.element.click()
        sleep(2)
    def cerraPestaña(self):
        self.google.close()
    def urlAtual(self):
        return self.google.current_url
    def introduccirDatos(self):
        self.element=self.google.find_element_by_name("email")
        self.element.send_keys(self.correo)
        sleep(2)
        self.element2=self.google.find_elements_by_class_name("form-control")[1]
        self.element2.send_keys(self.contraseña)
        self.element2.send_keys(Keys.RETURN)
        self.url2=self.google.find_element_by_name("//a")
        print(self.url2)
    
    

_url='https://b-ok.cc/book/841322/55519c'
google=buscadorGoogle(_url)
google.llamarGoogle()
#sleep(2)
#google.introduccirDatos()

#danielgrecia7@gmail.com