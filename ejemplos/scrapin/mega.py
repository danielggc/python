import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen("https://mega.nz/folder/6tFk2QTD#74KVdDyuMsF1c29zlVVtqw/folder/zxsHTYAQ")
url=BeautifulSoup(html,'html.parser')
artita_inisio=url.find(class_="files-grid-view fm select")

for artistas in artita_inisio:
    print(artistas.prettify())