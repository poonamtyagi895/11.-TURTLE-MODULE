from turtle import Turtle, Screen
tim = Turtle()
def move_forwards():
    tim.forward(8)
def move_backwards():
    tim.backward(8)
def counter_clockwise():
    tim.left(3)
def clockwise():
    tim.right(3)
def clear():
    screen.reset()
def penup():
    tim.penup()
def pendown():
    tim.pendown()
screen = Screen()
screen.listen()
screen.onkeypress(fun = move_forwards, key = "w")
screen.onkeypress(fun = move_backwards, key = "s")
screen.onkeypress(fun = counter_clockwise, key = "a")
screen.onkeypress(fun = clockwise, key = "d")
screen.onkey(fun = clear, key = "c")
screen.exitonclick()
