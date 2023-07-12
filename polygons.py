from turtle import Turtle, Screen
import random
timmy = Turtle()
colors = ["blue", "red", "green", "yellow", "pink", "grey", "purple", "brown", "black", "violet", "orange", "indigo"]
# timmy.speed(0)
timmy.hideturtle()
timmy.shape("turtle")
timmy.penup()
timmy.left(90)
timmy.forward(230)
timmy.right(90)
timmy.forward(40)
timmy.pendown()
def draw_shape(num_sides):
    angle=360/num_sides
    for _ in range(num_sides):
        timmy.right(angle)
        timmy.forward(100)
for shape_side_n in range(3, 11):
    timmy.color(random.choice(colors))
    draw_shape(shape_side_n)
screen = Screen()
screen.exitonclick()