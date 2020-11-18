from time import sleep
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.utils import keys_to_typing
from selenium.webdriver.common.keys import Keys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

profile=webdriver.FirefoxProfile('/home/dgc7/.mozilla/firefox/7aebrp31.dd7')
profile.set_preference("browser.download.panel.shown", False)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk","application/zip")
profile.set_preference("browser.download.folderList", 1) 
#ffprofile.setPreference("browser.download.folderList", 2); 
#ffprofile.setPreference("browser.download.dir", "/tmp");



google = webdriver.Firefox(profile)




correo='danielgrecia7@gmail.com'
contraseña='ddggcc77'
url='https://singlelogin.org/?logoutAll'
url2='https://b-ok.cc/dl/2271763/ee3d13'
google.get(url)
element=google.find_element_by_name("email")
element.send_keys(correo)
sleep(2)
element2=google.find_elements_by_class_name("form-control")[1]
element2.send_keys(contraseña)
element2.send_keys(Keys.RETURN)
sleep(5)
google.get('https://b-ok.cc/dl/616569/bca7f8')
element3= google

