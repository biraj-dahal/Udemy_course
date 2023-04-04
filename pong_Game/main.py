
from turtle import Screen
from Paddle import Paddle
from ball import Ball
import time
from ScoreBoard import Scoreboard
import os

screen = Screen()
screen.setup(width=1200, height=800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

user_paddle = Paddle((-550, 0))
comp_paddle = Paddle((550, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(key="w", fun=user_paddle.paddle_up)
screen.onkey(key="s", fun=user_paddle.paddle_down)
screen.onkey(key="Up", fun=comp_paddle.paddle_up)
screen.onkey(key="Down", fun=comp_paddle.paddle_down)

game_ended = False
while not game_ended:
    time.sleep(ball.sleep_time)
    screen.update()
    ball.move()

    if ball.ycor() > 375 or ball.ycor() < - 375:
        ball.bounce_y()
        os.system("afplay bounce.wav&")

    if (540 > ball.xcor() > 520 and comp_paddle.ycor()-50 < ball.ycor() < comp_paddle.ycor()+50) or (-540 < ball.xcor() < -520 and user_paddle.ycor()-50 < ball.ycor() < user_paddle.ycor()+50):
        ball.bounce_x()
        os.system("afplay bounce.wav&")

    if ball.xcor() > 560:
        ball.reset()
        score.user_point()

    if ball.xcor() < -560:
        ball.reset()
        score.comp_point()

    if score.user_score == 5:
        score.print_winner("Congratulations Left Side Wins.")
        game_ended = True
    elif score.comp_score == 5:
        score.print_winner("Congratulations Right Side Wins.")
        game_ended = True

screen.exitonclick()
