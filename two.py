import turtle
import math
import random

# Create screen
screen = turtle.Screen()
screen.title("Heart with Aishwarya")
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.tracer(0)

# Create turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(1)

# Colors
colors = ["red", "blue", "lime", "yellow", "magenta", "orange", "pink", "cyan"]

# Draw heart
for i in range(120):
    t.penup()
    t.goto(0, 0)

    angle = i * (2 * math.pi) / 120

    x = 16 * (math.sin(angle) ** 3) * 12
    y = (
        13 * math.cos(angle)
        - 5 * math.cos(2 * angle)
        - 2 * math.cos(3 * angle)
        - math.cos(4 * angle)
    ) * 12

    t.color(random.choice(colors))
    t.pendown()
    t.goto(x, y)

    # Small star at each point
    for _ in range(8):
        t.forward(6)
        t.backward(6)
        t.right(45)

# Write your name in the center
t.penup()
t.goto(0, -20)
t.color("white")
t.write("Aishwarya", align="center", font=("Arial", 24, "bold"))

# Show drawing
screen.update()

turtle.done()
