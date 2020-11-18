import requests
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
url='https://www.python.org/'
html=requests.get(url)
soup=BeautifulSoup(html.content,'html.parser')
for i in soup.find_all('p'):
    print(i)