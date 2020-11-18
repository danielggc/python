#estraes solo el texto de una pagina
import requests
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
url='https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-with-beautiful-soup-and-python-3'
html=requests.get(url)
soup=BeautifulSoup(html.content,'html.parser')
texto=soup.get_text()
print(texto)