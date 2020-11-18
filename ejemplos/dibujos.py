from turtle import Screen,Turtle
from math import sin,pi
pantalla=Screen()
pantalla.setup(825,425)
pantalla.screensize(800,400)
pantalla.setworldcoordinates(-2*pi,-1,2*pi,1)
tortuga =Turtle()

x=-2*pi
tortuga.penup()
tortuga.goto(x,sin(x))
tortuga.pendown()
while x<=2*pi:
    tortuga.goto(x,sin(x))
    x+=0.1


pantalla.exitonclick()