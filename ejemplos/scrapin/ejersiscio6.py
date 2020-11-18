import requests
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
url='https://www.python.org/'
html=requests.get(url)
texto=BeautifulSoup(html.content,'html.parser')
datoIl=texto.find_all('li')
for url in datoIl:
    link=url.find('a').attrs["href"]
    #print("\n")
    #print(link)
contador=0
https=list
for url in texto.find_all('li'):
    a=url.find('a')
    link=a.attrs['href']
    https=link
    print(link)
    contador+=1

