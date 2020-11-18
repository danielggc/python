
import re

string = 'foramulao 4uno 4fatoea'
#pattern = '(^h[a-z]+)'
#pattern = '^f[a-z]+'
#pattern = '^f[a-z]+a{1,3}'
#pattern = '((f|a|e|o)ora)[a-z]+'
#pattern = '\Afa[a-z]+'
#pattern = '\Afa[a-z]+'
#pattern = '\w'
#pattern = '^\d[a-z]+'
#pattern = '(^\d[a-z]+)o$'
pattern = '^\d[a-z]+o$'
for a in re.split('\s',string):
    #result = re.findall(pattern, a) 
    #result = re.sub(pattern,'hola',a) 
    #result = re.subn(pattern,'hola',a)  
    result=re.search(pattern,a)
    if result:
        print(result.group())

texto='holas d6anielas'
for a in  re.split('\s',texto):
    resultado2=re.search('^d.[a-z]+las\Z',a)
    if resultado2:
        print(resultado2.group())
