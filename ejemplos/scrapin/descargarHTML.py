import requests
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen("http://web.archive.org/web/20161022120719/http://www.nga.gov/collection/anB1.htm")
url=BeautifulSoup(html,'html.parser')
artita_inisio=url.find(class_="AlphaNav")
artista_final=artita_inisio.find_all('a')
escrituraDatos=csv.writer(open('artistas.csv','w'))
escrituraDatos.writerow(['name','link'])
for artistas in artista_final:
    links= 'https://web.archive.org'+ artistas.get('href')
    nombres=artistas.contents[0]
    print(links)
    print(nombres)
    escrituraDatos.writerow([nombres,links])
  