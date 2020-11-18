class permutacionParentesis():
    def __init__(self,_numeroParentesis:int,_diferencia):
        self.parentesisabiertos=_diferencia
        self.numeroParentesis:int=_numeroParentesis
    def primeraCapa(self,_cantidadParentesis:int)->int:
        self.cantidadParentesis=_cantidadParentesis
        self.respaldontidadParentesis=self.cantidadParentesis
        for self.d in range(0,self.cantidadParentesis):
            print("()",end="")
        print("fin",end="")
    def permutacionBacica(self):
        self.parentesisSobrantes=self.numeroParentesis
        self.numeroCapasTerminadas:int=1
        while self.numeroCapasTerminadas!=self.numeroParentesis:
            self.parentesisSobrantes-=1            
            self.permutaciones()

    def permutaciones(self):
        for self.i in range(0,self.parentesisSobrantes):
            parentesisEsternos(self.parentesisabiertos)
            for self.d in range(0,self.parentesisSobrantes):
                if self.d==self.i:
                    print("(",end="")
                    for self.y in range(0,self.numeroCapasTerminadas):
                        print("()",end="")
                    print(")",end="")
                else:
                    print("()",end="")
            parentesisserrados(self.parentesisabiertos)
            print("",end="fin")
        print("|",end="")
        self.numeroCapasTerminadas+=1


def parentesisEsternos(_numerentesis):
    diferencia=_numerentesis
    for l in range(diferencia):
        print("(",end="") 
def parentesisserrados(_numerentesis):
    diferencia=_numerentesis
    for l in range(diferencia):
        print(")",end="") 
numeroParentesis=4
permutaciones=permutacionParentesis(numeroParentesis,0)
respaldoParensis=numeroParentesis
permutaciones.primeraCapa(numeroParentesis)
while numeroParentesis!=0:
    print(" ")
    diferencia:int=respaldoParensis-numeroParentesis
    permutaciones=permutacionParentesis(numeroParentesis,diferencia)
    permutaciones.permutacionBacica()
    numeroParentesis-=1

