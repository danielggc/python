from math import sqrt
from turtle import Screen,Turtle

dirCordenada="/home/dgc7/ejersiciosLibros/pyaton/ejemplos/cordenadas.txt"
escrituraCordenada="/home/dgc7/ejersiciosLibros/pyaton/ejemplos/cordenadaTraducida.txt"
data= open(dirCordenada,'r')
escribir =open(escrituraCordenada,'r+')
entrada=False
x_inicial=0
y_inicial =0
movimiento_X=0
movimiento_Y=0
limite_X=0
limite_Y=0
for Line in data.readlines():
    for letter in Line.split(" "):
      print(letter)
      if entrada== False:
        x_inicial=int(letter[0])
        y_inicial=int(letter[2])
        entrada=True
        
      if entrada==True:
        movimiento_X=int(letter[0])
        movimiento_Y=int(letter[2])
        if movimiento_X> limite_X:
          diferecia=movimiento_X-limite_X
          limite_X=movimiento_X
          if diferecia==1:
             if movimiento_Y ==limite_Y:
                escribir.write("STOP\n")
                print("STOP\n")
             escribir.write("DR\n")
             print("DR\n") 
          else :
            for i in range(0,diferecia) :
              escribir.write("DR\n")
              print("DR\n")
            if movimiento_Y ==limite_Y:
                escribir.write("STOP\n")
                print("STOP\n")
        else:
          if movimiento_X<limite_X:
            diferecia= limite_X-movimiento_X
            limite_X=movimiento_X
            if diferecia==1:
              escribir.write("IZ\n")     
              print("IZ\n")
            else:
              for i in range(0,diferecia):
                escribir.write("IZ\n")
                print("IZ\n")
        if movimiento_Y>limite_Y:
          diferencia=movimiento_Y-limite_Y               
          limite_Y=movimiento_Y
          if diferencia==1:
            escribir.write("AR\nSTOP\n")
            print("AR\nSTOP\n")
          else:
            for i in range(0,diferencia):
              escribir.write("AR\n")
              print("AR\n")
            print("STOP\n")  
            escribir.write("STOP\n")
        else:
          if movimiento_Y<limite_Y:
            diferencia=limite_Y-movimiento_Y
            limite_Y=movimiento_Y
            if diferencia==1:
              escribir.write("AB\n")
              escribir.write("STOP\n")
              print("AB\nSTOP\n")
            else:
              for i in range (0,diferencia):
                escribir.write("AB\n")           
                print("AB\n")
              escribir.write("STOP\n")      
              print("STOP\n")
