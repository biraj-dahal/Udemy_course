from turtle import Turtle


class Ball(Turtle):
    sleep_time = 0.025

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.dx = 6
        self.dy = 6

    def move(self):
        new_x = self.xcor()+self.dx
        new_y = self.ycor()+self.dy
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1
        self.sleep_time *= 0.95

    def reset(self):
        self.goto(0, 0)
        self.bounce_x()
        self.sleep_time = 0.025

