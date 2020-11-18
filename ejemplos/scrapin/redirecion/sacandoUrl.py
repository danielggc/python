import requests

respuesta =requests.head("https://b-ok.cc/s/?q=c%2B%2B",allow_redirects=True)
for redireciones in respuesta:
    print(redireciones.url)
print(respuesta.url)    