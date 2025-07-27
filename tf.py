import turtle
import math

# Setup screen
screen = turtle.Screen()
screen.bgcolor('black')
turtle.colormode(255)

# Function to create a flower-drawing turtle
def create_flower_turtle():
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.pensize(1)
    return t

# Function to draw a flower at (x, y) with given color and rotation
def draw_flower(t, x, y, angle, size_scale=0.9, base_color=(255, 0, 0)):  # Bigger flowers
    t.penup()
    t.goto(x, y)
    t.setheading(angle)
    t.pendown()

    r_base, g_base, b_base = base_color
    for i in range(60):
        if i < 30:
            r = min(255, r_base + i * 2)
            g = min(255, g_base + i * 2)
            b = min(255, b_base + i * 2)
        else:
            r = max(0, r_base - (i - 30) * 2)
            g = max(0, g_base - (i - 30) * 2)
            b = max(0, b_base - (i - 30) * 2)
        t.pencolor(r, g, b)
        t.circle(-size_scale * (i + 1), 200)
        t.right(80)

# List of colors for different flowers
flower_colors = [
    (255, 0, 0),     # Red
    (255, 165, 0),   # Orange
    (255, 255, 0),   # Yellow
    (0, 255, 0),     # Green
    (0, 255, 255),   # Cyan
    (0, 0, 255),     # Blue
    (128, 0, 128),   # Purple
    (255, 105, 180), # Pink
    (255, 255, 255)  # White
]

# Center of bouquet placed at screen center
center_x = 0
center_y = 0
radius = 120  # Bigger circle for large flowers
num_flowers = 9

# Draw all flowers in a circular bouquet
for i in range(num_flowers):
    angle_deg = 360 / num_flowers * i
    angle_rad = math.radians(angle_deg)
    x = center_x + radius * math.cos(angle_rad)
    y = center_y + radius * math.sin(angle_rad)
    t = create_flower_turtle()
    draw_flower(t, x, y, angle=angle_deg, size_scale=0.9, base_color=flower_colors[i % len(flower_colors)])

# Draw the stem below the center
stem = turtle.Turtle()
stem.color("green")
stem.pensize(12)
stem.penup()
stem.goto(center_x, center_y - 30)
stem.setheading(-90)
stem.pendown()
stem.forward(250)

turtle.done()
