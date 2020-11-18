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
profile=webdriver.FirefoxProfile('/home/dgc7/.mozilla/firefox/7aebrp31.dd7')
profile.set_preference("browser.download.panel.shown", False)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk","application/zip")
profile.set_preference('browser.download.folderList',2)
profile.set_preference('browser.download.dir','/home/dgc7/zlibros/libros1920-1921')
proxies={
    "http":"http://169.57.157.146:8123",
    "https":"https://169.57.157.146:8123",
}
       
correo='danielgrecia7@gmail.com'
contraseña='ddggcc77'
google=webdriver.Firefox(profile)  
urlLoguin='https://singlelogin.org/?logoutAll'
google.get(urlLoguin)
element=google.find_element_by_name("email")
element.send_keys(correo)
sleep(2)
element2=google.find_elements_by_class_name("form-control")[1]
element2.send_keys(contraseña)
element2.send_keys(Keys.RETURN)

url='https://b-ok.cc/s/?yearFrom=1920&yearTo=1921'
html=requests.get(url,proxies=proxies)
carpetaUrl='/home/dgc7/Documentos/zlibrary/libros1920-1921/url'
try :
     os.mkdir(carpetaUrl)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
escribirURl=csv.writer(open('/home/dgc7/Documentos/zlibrary/libros1920-1921/url/url.csv','w'))
escribirUrlDowload=csv.writer(open('/home/dgc7/Documentos/zlibrary/libros1920-1921/url/urlDowload.csv','w'))
soup=BeautifulSoup(html.content,'html.parser')



for ulrPdf_Href in soup.find_all(itemprop = "name") :
    ulrPdf_Href=ulrPdf_Href.find('a',href=re.compile(''))
    urlPDf=ulrPdf_Href.get('href')
    urlPDf=re.sub('/book/','https://b-ok.cc/book/',urlPDf)
    escribirURl.writerow([urlPDf])
    print(urlPDf)
    for urlRedirec in range(0,1):
        google.get(urlPDf)
        sleep(5)
        htmlPDf=google.page_source
        soupRedirec=BeautifulSoup(htmlPDf,'html.parser')
        urlDownload=soupRedirec.find(class_="btn btn-primary dlButton addDownloadedBook")
        urlDownload=urlDownload.get('href')
        urlDownload=re.sub('/dl/','https://b-ok.cc/dl/',urlDownload)
        escribirUrlDowload.writerow([urlDownload])
        google.get(urlDownload)
        print(urlDownload)

