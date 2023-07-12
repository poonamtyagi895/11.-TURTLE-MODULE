import turtle
from turtle import Turtle, Screen
import random
directions = [0, 90, 180, 270]
turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color
timmy = Turtle()
timmy.pensize(15)
timmy.hideturtle()
timmy.speed(0)
for i in range(200):
    timmy.forward(30)
    timmy.color(random_color())
    timmy.setheading(random.choice(directions))
screen = Screen()
screen.exitonclick()