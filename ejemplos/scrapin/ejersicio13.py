#estraer cabesas de los hijos como meta li  code spanw
import requests
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
url='https://www.python.org/'
html=requests.get(url)
soup=BeautifulSoup(html.content,'html.parser')
for i in soup.recursiveChildGenerator():
    if i.name:
        print(i.name)
