import turtle
import math

def drawFiveCircles (turt, radius, centerX, centerY):
    turt.up
    turt.goto(centerX, centerY)
    turt.down()
    for i in range(5):
        sepalTurtle.begin_fill()
        sepalTurtle.circle(radius)
        sepalTurtle.end_fill()
        sepalTurtle.left(72)

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

drawFiveCircles(sepalTurtle,50,0,0)

drawFiveCircles(petalTurtle,25,0,0)

drawFiveCircles(centerTurtle,15,0, -15)


stampTurtle.up()
stampTurtle.goto(-2,0)
stampTurtle.down()
stampTurtle.stamp()

drawFiveCircles(sepalTurtle,50,0, 220)

drawFiveCircles(petalTurtle,25,0, 220)

drawFiveCircles(centerTurtle,15,0, 205)

stampTurtle.up()
stampTurtle.goto(-2,220)
stampTurtle.down()
stampTurtle.stamp()

drawFiveCircles(sepalTurtle,50,220, 0)

drawFiveCircles(petalTurtle,25,220, 0)

drawFiveCircles(centerTurtle,15,220, -15)

stampTurtle.up()
stampTurtle.goto(218,0)
stampTurtle.down()
stampTurtle.stamp()



drawFiveCircles(sepalTurtle,50,0, -220)

drawFiveCircles(petalTurtle,25,0, -220)

drawFiveCircles(centerTurtle,15,0, -235)

stampTurtle.up()
stampTurtle.goto(-2,-220)
stampTurtle.down()
stampTurtle.stamp()

sepalTurtle.up()
sepalTurtle.goto(-220, 0)
sepalTurtle.down()
for i in [0,1,2,3,4]:
    sepalTurtle.begin_fill()
    sepalTurtle.circle(50)
    sepalTurtle.end_fill()
    sepalTurtle.left(72)

petalTurtle.up()
petalTurtle.goto(-220, 0)
petalTurtle.down()
for i in [0,1,2,3,4]:
    sepalTurtle.begin_fill()
    sepalTurtle.circle(25)
    sepalTurtle.end_fill()
    sepalTurtle.left(72)

centerTurtle.up()
centerTurtle.goto(-220, -15)
centerTurtle.down()
centerTurtle.begin_fill()
centerTurtle.circle(15)
centerTurtle.end_fill()

stampTurtle.up()
stampTurtle.goto(-222,0)
stampTurtle.down()
stampTurtle.stamp()

win.exitonclick()