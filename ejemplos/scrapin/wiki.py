import requests
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

page = requests.get("https://en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer)")
soup = BeautifulSoup(page.content,'html.parser')
datosImagens=soup.find('img', {'src':re.compile('.jpg')})
print(datosImagens['src']+'\n')