from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    LEVEL = 1

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-550, y=350)
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"Level: {self.LEVEL}", align="left", font=FONT)

    def game_over_write(self):
        self.goto(x=-200, y=0)
        self.write(f"Game Over! \nSquish. You got hit by the car.", align="left", font=FONT)

