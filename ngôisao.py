import turtle
import random

t = turtle.Pen()
turtle.bgcolor("black")
t.speed(5)

colors = ["red", "yellow", "blue", "green", "orange", "white", "gray", "purple"]

for i in range(50):
    t.pencolor(random.choice(colors))
    size = random.randint(10, 40)
    x = random.randrange(-turtle.window_width() // 2, turtle.window_width() // 2)
    y = random.randrange(-turtle.window_height() // 2, turtle.window_height() // 2)

    t.penup()
    t.setpos(x, y)
    t.pendown()

    for m in range(5):
        t.forward(size * 2)
        t.right(144)

turtle.done()
