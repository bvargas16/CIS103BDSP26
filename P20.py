# Brian Vargas P20
from turtle import *
import time
def main():
    #first small circle
    bgcolor('white')
    color('red')
    shape('circle')
    speed(3)
    fillcolor('red')
    begin_fill()
    penup()
    #position is top left of bigger circle
    setposition(-100,100)
    pendown()
    circle(50)
    end_fill()

    #second big circle
    color('blue')
    fillcolor('blue')
    begin_fill()
    penup()
    #position is right of smaller circle
    setposition(50,100)
    pendown()
    circle(50)
    end_fill()

    #third big circle will enclose the other two circles
    color('green')
    shape('circle')
    penup()
    pensize(5)
    setposition(-15,-200)
    pendown()
    circle(250)
    
    #medium rectangle
    color('yellow')
    shape('square')
    fillcolor('yellow')
    begin_fill()
    penup()
    setposition(-50,-50)
    pendown()
    forward(100)
    left(90)
    forward(50)
    left(90)
    forward(150)
    left(90)
    penup()
    forward(50)
    left(90)
    forward(150)
    left(90)
    forward(50)
    end_fill()

    #upside down triangle
    color('black')
    shape('triangle')
    penup()
    pensize(20)
    setposition(-100,-160)
    pendown()
    right(90)
    forward(200)
    right(120)
    forward(200)
    right(120)
    forward(200)
    time.sleep(5)

main()