import turtle
import random

turtle.setup(800, 800)
turtle.bgcolor("white")
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.width(2)
turtle.tracer(False)

colors = ["skyblue", "lightpink", "gold", "lightgreen"]

def draw_petal(radius, angle):
    for _ in range(2):
        t.circle(radius, angle)
        t.left(180 - angle)

def draw_flower(petals, radius, angle):
    for _ in range(petals):
        t.color(random.choice(colors))
        draw_petal(radius, angle)
        t.right(360 / petals)

layers = [
    (12, 100, 60),
    (24, 70, 80),
    (36, 40, 100)
]

for petals, radius, angle in layers:
    t.penup()
    t.goto(0, 0)
    t.pendown()
    draw_flower(petals, radius, angle)
    t.right(10)

t.penup()
t.goto(-10, -20)
t.pendown()
t.color("gold")
t.begin_fill()
t.circle(20)
t.end_fill()

turtle.tracer(True)
turtle.done()
