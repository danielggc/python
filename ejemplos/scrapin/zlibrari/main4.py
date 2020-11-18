from bs4 import BeautifulSoup
import re
import requests
from time import sleep
proxies={
    "http":"http://103.83.116.170:55443",
    "https":"https://103.83.116.170:55443",
}
  
urlPDf='https://b-ok.cc/ireader/841322'
htmlPDf=requests.get(urlPDf)
soupRedirec=BeautifulSoup(htmlPDf.content,'html.parser')
print(soupRedirec)