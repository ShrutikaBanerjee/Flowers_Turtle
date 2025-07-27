import turtle
import colorsys

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

h = 0
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(c)
    t.circle(100)
    t.left(1)
    h += 0.002

turtle.done()
