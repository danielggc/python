from math import sqrt
from turtle import Screen,Turtle
class variable:
    def __init__ (self):
        self.escrituraCordenada="/home/dgc7/ejersiciosLibros/pyaton/ejemplos/cordenadaTraducida.txt"
        self.escribir =open(self.escrituraCordenada,'r+')
        self.x_inicial=0
        self.y_inicial =0
        self.movimiento_X=0
        self.movimiento_Y=0
        self.limite_X=0
        self.limite_Y=0
class escrituraCordenadas(variable):
    def __init__(self):
        super().__init__()
    def coredaInicial(self):
       self.x_inicial=int(letter[0])
       self.y_inicial=int(letter[2])
       self.entrada=True    
    def movimientoDR(self,_movimiento_X,_movimiento_y):
        self.movimiento_X=_movimiento_X
        self.movimiento_Y=_movimiento_y
        if self.movimiento_X> self.limite_X:    
          self.diferecia=self.movimiento_X-self.limite_X
          self.limite_X=self.movimiento_X
          if self.diferecia==1:
             if self.movimiento_Y ==self.limite_Y:
                self.escribir.write("STOP\n")
                print("STOP\n")
             self.escribir.write("DR\n")
             print("DR\n") 
          else:
            for self.i in range(0,self.diferecia) :
              self.escribir.write("DR\n")
              print("DR\n")
            if self.movimiento_Y ==self.limite_Y:
                self.escribir.write("STOP\n")
                print("STOP\n")  
    def movimientoIZ(self,_movimiento_X):
           self.movimiento_X=_movimiento_X
           if self.movimiento_X<self.limite_X:
            self.diferecia= self.limite_X-self.movimiento_X
            self.limite_X=self.movimiento_X
            if self.diferecia==1:
              self.escribir.write("IZ\n")     
              print("IZ\n")
              if self.movimiento_Y ==self.limite_Y:
                self.escribir.write("STOP\n")
                print("STOP\n")         
            else:
              for self.i in range(0,self.diferecia):
                self.escribir.write("IZ\n")
                print("IZ\n") 
              if self.movimiento_Y ==self.limite_Y:
                self.escribir.write("STOP\n")
                print("STOP\n")
            
    def movimientoAR(self,_movimiento_Y):
        if self.movimiento_Y>self.limite_Y:
            self.movimiento_Y=_movimiento_Y
            self.diferencia=self.movimiento_Y-self.limite_Y               
            self.limite_Y=self.movimiento_Y
            if self.diferencia==1:
                self.escribir.write("AR\nSTOP\n")
                print("AR\nSTOP\n")
            else:
                for self.i in range(0,self.diferencia):
                    self.escribir.write("AR\n")
                    print("AR\n")
                print("STOP\n")  
                self.escribir.write("STOP\n")   
    def movimientoAB(self,_movimiento_y):
        self.movimiento_Y=_movimiento_y
        if self.movimiento_Y<self.limite_Y:
            self.diferencia=self.limite_Y-self.movimiento_Y
            self.limite_Y=self.movimiento_Y
            if self.diferencia==1:
              self.escribir.write("AB\n")
              self.escribir.write("STOP\n")
              print("AB\nSTOP\n")
            else:
              for self.i in range (0,self.diferencia):
                self.escribir.write("AB\n")           
                print("AB\n")
              self.escribir.write("STOP\n")      
              print("STOP\n")

dirCordenada="/home/dgc7/ejersiciosLibros/pyaton/ejemplos/cordenadas.txt"
data= open(dirCordenada,'r')
entrada=True
datos=escrituraCordenadas()
for Line in data.readlines():
    for letter in Line.split(" "):
        print(letter)  
        if entrada== False:
            datos.coredaInicial()
            entrada=True
        if entrada==True:
            x=int(letter[0])
            y=int(letter[2])
            datos.movimientoDR(x,y)
            datos.movimientoIZ(x)
            datos.movimientoAR(y)
            datos.movimientoAB(y)
            

        



            