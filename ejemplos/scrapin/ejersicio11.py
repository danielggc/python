import requests
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
url='https://www.python.org/'
html=requests.get(url)
soup=BeautifulSoup(html.content,'html.parser')
for d in range(1,4):
    for i in soup.find_all('h'+str(d)):
        print(i)