# snow flake

from turtle import *

shape("turtle")
shapesize(0.8)
speed(0)


def snowflake(length, levels):
    if levels == 0:
        forward(length)
        return

    length /= 3.0
    snowflake(length, levels - 1)
    left(60)
    snowflake(length, levels - 1)
    right(120)
    snowflake(length, levels - 1)
    left(60)
    snowflake(length, levels - 1)


def create_snowflake(sides, length):

    for i in range(sides):
        snowflake(length, sides)
        right(360 / sides)


create_snowflake(3, 200)
penup()
goto(-300, 200)
pendown()
create_snowflake(3, 200)

mainloop()



