from turtle import Turtle, Screen


def forward():
    brz.forward(10)


def backward():
    brz.backward(10)


def clockwise():
    brz.right(10)


def anticlockwise():
    brz.left(10)


def clear_screen():
    brz.penup()
    brz.clear()
    brz.setheading(0)
    brz.goto(0, 0)
    brz.pendown()


screen = Screen()
brz = Turtle()
brz.shape("turtle")
brz.speed("fast")
screen.listen()
screen.onkey(key='a', fun=anticlockwise)
screen.onkey(key='d', fun=clockwise)
screen.onkey(key='w', fun=forward)
screen.onkey(key='s', fun=backward)
screen.onkey(key='c', fun=clear_screen)

screen.exitonclick()
