def url(x,y):
    urlAños='https://b-ok.cc/s/?yearFrom='+str(x)+'&yearTo='+str(y)
    print(urlAños)
url(1921,1922)


class numeros:
    def __init__(self):
        self.dato=2
    def pares(self,numero):
        self.resultado=numero*self.dato
        return self.resultado

d=numeros()
a=d.pares(4)            
print(a)
