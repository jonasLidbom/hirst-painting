import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255) # Changes mode so we can use rgb colors.

color_list = [(199, 175, 117), (124, 36, 24), (168, 106, 57), (222, 224, 227),
 (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36),
 (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155),
 (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82),
 (46, 73, 62), (47, 66, 82)]

t = Turtle()
t.penup()

x = -250
y = -250

for _ in range(10):
    t.goto(x, y)
    for _ in range(10):
        t.dot(20, random.choice(color_list))
        t.forward(50)
    y += +50

screen = Screen()
screen.exitonclick()


