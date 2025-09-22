import turtle
import math

def drawFiveCircles (turt, radius, centerX, centerY):
    turt.up()
    turt.goto(centerX, centerY)
    turt.down()
    for i in range(5):
        turt.begin_fill()
        turt.circle(radius)
        turt.end_fill()
        turt.left(72)

win = turtle.Screen()
win.bgcolor("light sky blue")

sepalTurtle = turtle.Turtle()
sepalTurtle.speed(0)
sepalTurtle.color("dark green", "spring green")
sepalTurtle.hideturtle()

petalTurtle = turtle.Turtle()
petalTurtle.speed(0)
petalTurtle.color('dark red', 'light coral')
petalTurtle.hideturtle()

centerTurtle = turtle.Turtle()
centerTurtle.speed(0)
centerTurtle.color('purple4')
centerTurtle.hideturtle()

stampTurtle = turtle.Turtle()
stampTurtle.color("gold")
stampTurtle.speed(0)
stampTurtle.shape("turtle")
stampTurtle.hideturtle()

positions = [(0,0), (0,220), (220,0), (0,-220), (-220,0)]
for (x,y) in positions:
    drawFiveCircles(sepalTurtle, 50, x, y)
    drawFiveCircles(petalTurtle, 25, x, y)

    centerTurtle.up()
    centerTurtle.goto(x,y-15)
    centerTurtle.down()
    centerTurtle.begin_fill()
    centerTurtle.circle(15)
    centerTurtle.end_fill()

    stampTurtle.up()
    stampTurtle.goto(x-2, y)
    stampTurtle.stamp()

win.exitonclick()