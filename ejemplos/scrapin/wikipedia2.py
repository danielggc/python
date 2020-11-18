import requests
import csv
import re
import wget
import shutil
from urllib.request import urlopen
from bs4 import BeautifulSoup
url='https://es.wikipedia.org/wiki/Imagen'
html=requests.get(url)
soup=BeautifulSoup(html.content,'html.parser')
img_url=soup.find_all('img',class_="thumbimage",src=re.compile('jpg|png|gif|.bmp|.JPG|.PNG|.GIF|.BMP'))
img_url2=soup.find('img',class_="thumbimage",src=re.compile('.jpg'))
escrituraDatos=csv.writer(open('imagenes.csv','w'))
escrituraDatos.writerow(['link'])
contador=0
for image in img_url:
    contador+=1
    image=image.get('src')
    imprimirImagen=re.sub('//upload.wikimedia.','https://upload.wikimedia.',image)
    print(imprimirImagen)
    escrituraDatos.writerow([imprimirImagen])
    resp =requests.get(imprimirImagen,stream=True)
    local_file=open('/home/dgc7/Imágenes/imagenesPrueba/prueba'+str(contador)+'.png','wb')
    resp.raw.decode_content=True
    shutil.copyfileobj(resp.raw,local_file)
