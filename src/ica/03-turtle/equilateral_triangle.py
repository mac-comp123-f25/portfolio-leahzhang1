import turtle
window = turtle.Screen()
ian = turtle.Turtle()
window.bgcolor("pink")
ian.color("black")
ian.begin_fill()
for i in range(2):
    ian.forward(100)
    ian.left(120)
ian.forward(100)
ian.end_fill()
turtle.done()