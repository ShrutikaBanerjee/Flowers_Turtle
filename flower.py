import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor('black')
t.speed(0)
t.pensize(2)
t.hideturtle()  # Optional: hides the turtle arrow
turtle.colormode(255)  # Enable RGB mode

for i in range(300):
    # Red to Yellow to Green gradient (255,0,0) → (255,255,0) → (0,255,0)
    if i < 150:
        r = 255
        g = int(i * (255 / 150))  # 0 to 255
        b = 0
    else:
        r = int(255 - ((i - 150) * (255 / 150)))  # 255 to 0
        g = 255
        b = 0

    t.pencolor(r, g, b)
    t.circle(-i + 1, 200)
    t.right(80)

turtle.done()
