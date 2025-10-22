import turtle
window = turtle.Screen()
t = turtle.Turtle()
window.bgcolor("lavender")
t.color("blue")
for i in range(5):
  t.forward(100)
  t.right(144)

leah = turtle.Turtle()
window.bgcolor("lavender")
leah.penup()
leah.goto(-200,0)
leah.pendown()
leah.color("black")
for i in range(5):
      leah.forward(100)
      leah.right(144)