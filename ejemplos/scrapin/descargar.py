import wget
import requests
import shutil
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/220px-Image_created_with_a_mobile_phone.png"
url2=url = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Ernst_Mach_Innenperspektive.png/220px-Ernst_Mach_Innenperspektive.png"
url3="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Shadow_2752.jpg/220px-Shadow_2752.jpg"
#for i in range(0,6):
 #   wget.download(url,'/home/dgc7/Imágenes/imagenesPrueba/prueba'+str(i)+'.png')
resp =requests.get(url2,stream=True)
local_file=open('/home/dgc7/Imágenes/imagenesPrueba/prueba'+'.png','wb')
resp.raw.decode_content=True
for i in range(0,5):
    resp =requests.get(url2,stream=True)
    local_file=open('/home/dgc7/Imágenes/imagenesPrueba/prueba'+str(i)+'.png','wb')
    resp.raw.decode_content=True
    shutil.copyfileobj(resp.raw,local_file)