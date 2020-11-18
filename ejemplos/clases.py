class pajaro:
    def __init__(self,_nombre,_clase):
        self.nombre=_nombre
        self.clase=_clase
        print(self.nombre)
        print(self.clase)
class guacamaya(pajaro) :
    def __init__(self,nombre,clase):
        super().__init__(nombre,clase)
    def hablar(self):
        self.nombre="hola"
        return "abilidad lenguistica baja"
    def nombres(self):
        print(self.nombre)
class duplicar:
    def __init__(self,_numero):
        self.numero=_numero
        self.constante=2
    def multiplicar(self):
        self.valor2=self.numero*self.constante
        return self.valor2
pajaro1=pajaro('azul','agas')  
pajaro2=guacamaya("trifio","guacamaya")
print(pajaro2.hablar())  
pajaro2.nombres()    
dato=123
valor=duplicar(dato)        
datoMultiplicado=valor.multiplicar()
print(datoMultiplicado)