import turtle
def draw_nested_squares (turt):
    for size in range(10,90,10):
        for _ in range(4):
            turt.right(90)
            turt.backward(size)
        turt.penup()
        turt.pendown()
win = turtle.Screen()
tt = turtle.Turtle()
draw_nested_squares(tt)
win.exitonclick()




