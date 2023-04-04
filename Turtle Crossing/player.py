from turtle import Turtle

MOVE = 10
STARTING_POS = (0, -380)
FINISH_LINE_Y = 380


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.reset_pos()

    def move(self):
        self.forward(MOVE)

    def finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def reset_pos(self):
        self.goto(STARTING_POS)



