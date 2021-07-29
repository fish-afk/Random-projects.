# a fractal is a curve or a geometric figure, each part of which has the same patterns
# recur at progressively smaller scales...
# the turtle module is a 2D graphics module in python

from turtle import *

shape("turtle")
shapesize(0.8)
speed(1)


def tree(size, levels, angle):
    if levels == 0:
        color("green")
        dot(size)
        color("black")
        return

    forward(size)
    right(angle)

    tree(size * 0.8, levels - 1, angle)

    left(angle * 2)
    tree(size * 0.8, levels - 1, angle)

    right(angle)
    backward(size)


left(90)
tree(70, 7, 30)

mainloop()


