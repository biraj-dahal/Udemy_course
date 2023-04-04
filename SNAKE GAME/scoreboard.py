from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, level):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.level = level
        self.goto(x=0, y=360)
        self.levels_highscore=[0, 0, 0]
        self.update_scoreboard()

    def get_highscore(self):
        with open("highscore.txt", 'r+') as f:
            for num in f:
                self.levels_highscore[0], self.levels_highscore[1], self.levels_highscore[2] = num.split()

        if self.level == "e":
            return self.levels_highscore[0]
        elif self.level == "h":
            return self.levels_highscore[2]
        return self.levels_highscore[1]

    def update_scoreboard(self):
        self.clear()
        self.get_highscore()
        self.write(f"Your Score: {self.score}   High Score:{self.get_highscore()}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        if self.score > int(self.get_highscore()):
            if self.level == "e":
                self.levels_highscore[0] = self.score
            elif self.level == "h":
                self.levels_highscore[2] = self.score
            else:
                self.levels_highscore[1] = self.score

            with open("highscore.txt", 'w') as f:
                f.write(f"{self.levels_highscore[0]} {self.levels_highscore[1]} {self.levels_highscore[2]}")
        self.write("GAME OVER!", align="center", font=("Arial", 24, "normal"))



