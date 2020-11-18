import requests
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
url="http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html"
http=urlopen(url)
imagenesHTTP=BeautifulSoup(http,"html.parser")
datos=imagenesHTTP.find_all(id="first")
datos2=imagenesHTTP.select("div p")
print(imagenesHTTP)
print("\n\n\n")
print(datos2)
