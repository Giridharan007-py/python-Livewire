import turtle

# Set up screen
screen = turtle.Screen()
screen.title("CSK with Turtle!")
screen.bgcolor("#dadd2f")  # Dark blue background

# Create turtle
pen = turtle.Turtle()
pen.pensize(8)
pen.speed(2)
pen.color("gold")  # CSK theme color

# Draw letter C
def draw_C():
    pen.penup()
    pen.goto(-250, 0)
    pen.setheading(0)
    pen.pendown()
    pen.circle(50, 180)

# Draw letter S
def draw_S():
    pen.penup()
    pen.goto(-100, 50)
    pen.setheading(0)
    pen.pendown()
    pen.circle(25, 180)
    pen.circle(-25, 180)

# Draw letter K
def draw_K():
    pen.penup()
    pen.goto(50, -50)
    pen.setheading(90)
    pen.pendown()
    pen.forward(100)

    pen.backward(50)
    pen.right(45)
    pen.forward(70)

    pen.backward(70)
    pen.right(90)
    pen.forward(70)

# Draw each letter
draw_C()
draw_S()
draw_K()

# Add finishing text
pen.penup()
pen.goto(-100, -150)
pen.color("white")
pen.write("Chennai Super Kings", align="center", font=("Arial", 24, "bold"))

# Hide turtle and display window
pen.hideturtle()
screen.mainloop()
