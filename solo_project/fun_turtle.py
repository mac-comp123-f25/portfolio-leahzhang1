import turtle
import random

t = turtle.Turtle()
t.speed(0)
screen = turtle.Screen()
screen.bgcolor("black")


def get_user_input():
    size = screen.numinput("Tree Size", "Enter trunk length (60-150):", 100, 60, 150)
    depth = screen.numinput("Tree Depth", "Enter recursion depth (4-8):", 6, 4, 8)

    color_choice = screen.textinput("Color", "1=Brown/Green, 2=Autumn, 3=Random:")
    if color_choice == "1":
        colors = ["#8B4513", "#2E8B57", "#228B22", "#32CD32", "#90EE90"]
    elif color_choice == "2":
        colors = ["#8B4513", "#A0522D", "#CD853F", "#FF4500", "#FFD700"]
    else:
        colors = ["#{:06x}".format(random.randint(0, 0xFFFFFF)) for _ in range(5)]

    return size, int(depth), colors


def draw_tree(branch_len, depth, colors, angle=25):
    if depth == 0:
        return

    color_index = min(depth, len(colors) - 1)
    t.pencolor(colors[color_index])
    t.pensize(depth * 1.2)

    t.forward(branch_len)

    if depth > 1:
        t.right(angle)
        draw_tree(branch_len * 0.7, depth - 1, colors, angle + random.uniform(-5, 5))

        t.left(angle * 2)
        draw_tree(branch_len * 0.7, depth - 1, colors, angle + random.uniform(-5, 5))

        t.right(angle)

    t.backward(branch_len)


def main():
    size, depth, colors = get_user_input()

    t.penup()
    t.goto(0, -200)
    t.setheading(90)
    t.pendown()

    draw_tree(size, depth, colors)
    t.hideturtle()
    screen.exitonclick()

main()