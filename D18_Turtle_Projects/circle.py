from turtle import Turtle, Screen, color, colormode
import random
turtle = Turtle()
screen = Screen()
turtle.shape('turtle')
turtle.color('black')

colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)


draw_spirograph(5)
