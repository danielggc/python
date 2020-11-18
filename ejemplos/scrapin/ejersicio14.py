#estraer cabesas de los hijos como meta li  code spanw
import requests
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
url='https://www.python.org/'
html=requests.get(url)
soup=BeautifulSoup(html.content,'html.parser')
#ht=soup.find_all(attrs={"class":"tier-1 element-1"})
print(soup)

#print(ht)
texto2='<input name="email"/>'
name_soup = BeautifulSoup(texto2,'html.parser')
#print(name_soup.find_all(attrs={"name": "email"}))
# [<input name="email"/>]
#texto3=soup.find_all(class_=re.compile("ier-2"))
#print(texto2)
print("\n\n\n\n\n\n\n\n\n\n\n")
#texto3=soup.select("li.tier-2.element-1")
#print(texto3)
#    return css_class is not None and len(css_class) == 6
#texto3=soup.find_all('span',class_='pre')
#texto3=soup.find_all('span',attrs={'class':'pre'})
#print(texto3)
#texto3=soup.find_all('a',href='https://status.python.org/')
#texto3=soup.find_all('a',class_='jump-link')
#texto3=soup.find_all('a',class_='jump-link',limit=7)
#texto3=soup.title.find_all(string=True)
#texto3=soup.title(string=True)
texto4=soup.head.title
texto3=soup.find("head").find("title")
print(texto3)
print(texto4)
