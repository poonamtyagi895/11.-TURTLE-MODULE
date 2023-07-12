import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
timmy = Turtle()
timmy.hideturtle()
timmy.speed(0)
def draw_spirograph(size):
    for i in range(int(360/size)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size)
draw_spirograph(2)
screen = Screen()
screen.exitonclick()