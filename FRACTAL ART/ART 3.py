from turtle import *

shape("turtle")
shapesize(0.8)
speed(1)


def triangle(length, angle=120):

    forward(length)
    left(angle)
    forward(length)
    left(angle)
    forward(length)


def triangle2and3():
    right(120)
    triangle(385)
    right(120)
    triangle(385)
    right(30)
    color("red")
    dot(40)
    color("black")
    forward(385/2)
    left(120)
    triangle(385)
    right(180)
    triangle(385)


triangle(385)
triangle2and3()



mainloop()