import requests

url = 'https://b-ok.cc/dl/1240102/5dc623'

myfile = requests.get(url, allow_redirects=True)

open('/home/dgc7/hello3.pdf', 'wb').write(myfile.content)