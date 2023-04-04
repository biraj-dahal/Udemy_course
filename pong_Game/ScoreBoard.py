from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.user_score = 0
        self.comp_score = 0
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.user_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.comp_score, align="center", font=("Courier", 80, "normal"))

    def user_point(self):
        self.user_score += 1
        self.update_score_board()

    def comp_point(self):
        self.comp_score += 1
        self.update_score_board()

    def print_winner(self, prompt):
        self.clear()
        self.goto(0, 0)
        self.write(prompt, align="center", font=("Courier", 50, "normal"))

