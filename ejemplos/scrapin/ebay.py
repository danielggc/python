import requests
import csv
import re
import wget
import shutil
from urllib.request import urlopen
from bs4 import BeautifulSoup
url='https://apps.auction123.com/ImageViewer/ImgViewer.aspx?aID=3979019&sID=0'
html=requests.get(url)
soup=BeautifulSoup(html.content,'html.parser')
img_urlJPG=soup.find_all('img',src=re.compile('.jpg|.jpg'))
img_url=soup.find_all('img',src=re.compile('.jpg|.jpg|.png|gif|.bmp|.JPG|.PNG|.GIF|.BMP'))
contador=0
escrituraDatos=csv.writer(open('/home/dgc7/Imágenes/daemon/pruebaimagenDaemon.csv','w'))
for image in img_url:
    image=image.get('src')
    escrituraDatos.writerow([image])
    print(image)

for image in img_urlJPG:
    contador+=1
    image=image.get('src')
    if re.match('https://',image):
        print("hola")
        resp =requests.get(image,stream=True)
        local_file=open('/home/dgc7/Imágenes/daemon/prueba'+str(contador)+'.jpg','wb')
        resp.raw.decode_content=True
        shutil.copyfileobj(resp.raw,local_file)
        print(image)
    else :
        image=re.sub('//','https://',image)
        image=re.sub('webimage001s','webimage001l',image)
        resp =requests.get(image,stream=True)
        local_file=open('/home/dgc7/Imágenes/daemon/prueba'+str(contador)+'.jpg','wb')
        resp.raw.decode_content=True
        shutil.copyfileobj(resp.raw,local_file)
        print(image)
img_urlPNG=soup.find_all('img',src=re.compile('.png|.PNG'))
for image in img_urlPNG:
    if re.match('https://',image):
        contador+=1
        image=image.get('src')
        resp =requests.get(image,stream=True)
        local_file=open('/home/dgc7/Imágenes/daemo/prueba'+str(contador)+'.png','wb')
        resp.raw.decode_content=True
        shutil.copyfileobj(resp.raw,local_file)
        print(image)    
    else :
        contador+=1
        image=image.get('src')
        image=re.sub('//','https://',image)
        resp =requests.get(image,stream=True)
        local_file=open('/home/dgc7/Imágenes/daemon/prueba'+str(contador)+'.png','wb')
        resp.raw.decode_content=True
        shutil.copyfileobj(resp.raw,local_file)
        print(image)  
img_urlGIF=soup.find_all('img',src=re.compile('.gif|.GIF'))
for image in img_urlGIF:
    if re.match('https://',image):
        contador+=1
        image=image.get('src')
        escrituraDatos.writerow([image])
        resp =requests.get(image,stream=True)
        local_file=open('/home/dgc7/Imágenes/daemon/prueba'+str(contador)+'.gif','wb')
        resp.raw.decode_content=True
        shutil.copyfileobj(resp.raw,local_file)
        print(image)
    else :
        contador+=1
        image=image.get('src')
        image=re.sub('//','https://',image)
        escrituraDatos.writerow([image])
        resp =requests.get(image,stream=True)
        local_file=open('/home/dgc7/Imágenes/daemon/prueba'+str(contador)+'.gif','wb')
        resp.raw.decode_content=True
        shutil.copyfileobj(resp.raw,local_file)
        print(image)
img_urlBMB=soup.find_all('img',src=re.compile('.bmb|.BMB'))
for image in img_urlBMB:
    if re.match('https://',image):
        contador+=1
        image=image.get('src')
        resp =requests.get(image,stream=True)
        local_file=open('/home/dgc7/Imágenes/daemon/prueba'+str(contador)+'.bmb','wb')
        resp.raw.decode_content=True
        shutil.copyfileobj(resp.raw,local_file)
        print(image)
    else :
        contador+=1
        image=image.get('src')
        image=re.sub('//','https://',image)
        resp =requests.get(image,stream=True)
        local_file=open('/home/dgc7/Imágenes/daemon/prueba'+str(contador)+'.bmb','wb')
        resp.raw.decode_content=True
        shutil.copyfileobj(resp.raw,local_file)
        print(image)


#png|.png|gif|.bmp|.JPG|.PNG|.GIF|.BMP'
   