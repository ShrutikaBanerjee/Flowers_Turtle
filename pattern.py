import turtle

# Create turtle object
tree = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
tree.color("green")
tree.speed(0)  # Fastest drawing speed

# Recursive function to draw a tree
def draw_branch(branch_length):
    if branch_length > 5:
        tree.forward(branch_length)
        tree.right(20)
        draw_branch(branch_length - 15)
        tree.left(40)
        draw_branch(branch_length - 15)
        tree.right(20)
        tree.backward(branch_length)

# Position turtle
tree.left(90)  # Point upwards
tree.up()
tree.backward(100)  # Move back without drawing
tree.down()

# Draw tree
draw_branch(100)

# End program on click
screen.exitonclick()
