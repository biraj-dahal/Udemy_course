from turtle import Turtle


class Paddle(Turtle):
    move = 27

    def __init__(self, location=(0, 0)):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.goto(location)
        self.shapesize(stretch_wid=7, stretch_len=1)

    def paddle_up(self):
        if self.ycor() <= 300:
            self.goto(x=self.xcor(), y=self.ycor()+self.move)

    def paddle_down(self):
        if self.ycor() >= -300:
            self.goto(x=self.xcor(), y=self.ycor()-self.move)

