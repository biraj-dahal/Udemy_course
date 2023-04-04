from turtle import Screen, Turtle
import time
from SNAKE import SNAKE
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.title("Snake eats the turtle")
screen.setup(height=800, width=800)
screen.bgcolor("black")
screen.tracer(0)

border = Turtle()
border.hideturtle()
border.penup()
border.speed("fast")
border.goto(x=-400, y=350)
border.color("white")
border.pendown()
border.forward(800)

snake = SNAKE()
food = Food()

level = screen.textinput(title="Choose Difficulty", prompt="E for Easy, M for Medium, and H for Hard.").lower()
if level == "e":
    SLEEP = 0.12
elif level == "h":
    SLEEP = 0.05
else:
    SLEEP = 0.1

score_board = Scoreboard(level)

screen.listen()
screen.onkey(key="Up", fun=snake.change_up)
screen.onkey(key="Down", fun=snake.change_down)
screen.onkey(key="Right", fun=snake.change_right)
screen.onkey(key="Left", fun=snake.change_left)

game_ended = False
while not game_ended:
    screen.update()
    time.sleep(SLEEP)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh_food()
        snake.extend()
        score_board.increase_score()

    if snake.head.xcor() > 399 or snake.head.xcor() < -399 or snake.head.ycor() < -399 or snake.head.ycor() > 350:
        game_ended = True
        score_board.game_over()

    for each_block in snake.snake_block[1:]:
        if snake.head.distance(each_block) < 10:
            game_ended = True
            score_board.game_over()

screen.exitonclick()
