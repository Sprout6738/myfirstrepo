import turtle

# Create a turtle object
t = turtle.Turtle()

# Set turtle speed and pen color
t.speed(0)  # Set the speed to the maximum
t.pensize(5)  # Set the pen size

# Function to draw a square with a given side length
def draw_square(side_length):
    for _ in range(4):
        t.forward(side_length)
        t.right(90)

# Function to draw the creeper face
def draw_creeper_face():
    # Draw the outer square
    t.fillcolor("lime")
    t.begin_fill()
    draw_square(100)
    t.end_fill()

    # Draw the eyes
    t.penup()
    t.goto(30, 60)  # Position the turtle at the right eye
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    draw_square(20)
    t.end_fill()

    t.penup()
    t.goto(-30, 60)  # Position the turtle at the left eye
    t.pendown()
    t.begin_fill()
    draw_square(20)
    t.end_fill()

    # Draw the mouth
    t.penup()
    t.goto(-30, 30)  # Position the turtle at the mouth
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    draw_square(60)
    t.end_fill()

# Draw the creeper face
draw_creeper_face()

# Hide the turtle and keep the window open
t.hideturtle()
turtle.done()
