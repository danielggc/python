
import requests
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
url='https://www.python.org/'
html=requests.get(url)
soup=BeautifulSoup(html.content,'html.parser')
contador=0
for i in soup.find_all('h2'):
    if contador<4:
        contador+=1
       # print(i)
print(soup.find_all('h2')[0:4])