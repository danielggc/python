from math import sqrt
from turtle import Screen,Turtle

pantalla=Screen()
pantalla.setup(1025,1025)
pantalla.screensize(1000,1000)
pantalla.setworldcoordinates(-500,-500,500,500)
pantalla.delay(0)


x1=-200
y1=-200
velocidad_x1=0.1
velocidad_y1=0
m1=20
x2=200
y2=200
velocidad_x2=-0.1
velocidad_y2=0
m2=20


cuerpo1=Turtle('circle')
cuerpo1.color('red')
cuerpo1.speed(0)
cuerpo1.penup()
cuerpo1.goto(x1,y1)
cuerpo1.pendown()

cuerpo2=Turtle('circle')
cuerpo2.color('blue')
cuerpo2.speed(0)
cuerpo2.pendown()
cuerpo2.goto(x2,y2)
cuerpo2.pendown()

radio=100
contador_x=radio
contador_y=0

for t in range(10000):
    if contador_x<2*radio:
        x1+=0.1
        contador_x+=0.1
    else :
        if contador_x >radio:
            x1-=0.5
    if contador_y<2*radio:
        y1+=0.1
        contador_y+=0.1
    cuerpo1.goto(x1,y1)
    cuerpo2.goto(x2,y2)

pantalla.exitonclick()
