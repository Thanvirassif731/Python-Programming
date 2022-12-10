import turtle

square_turtle = turtle.Turtle()

def call_me():
    square_turtle.forward(100)
    square_turtle.left(90)
    square_turtle.forward(100)
    square_turtle.left(90)
    square_turtle.forward(100)
    square_turtle.left(90)
    square_turtle.forward(100)
    square_turtle.left(90)

call_me()
square_turtle.forward(200)
call_me()