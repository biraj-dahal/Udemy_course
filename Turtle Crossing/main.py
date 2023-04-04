from player import Player
from scoreboard import Scoreboard
from car_manager import Cars
from turtle import Screen
import time

PROXIMITY = 40

screen = Screen()
screen.title("Turtle Crossing Game")
screen.bgcolor("white")
screen.setup(width=1200, height=800)
screen.tracer(0)

player = Player()
car = Cars()
score = Scoreboard()

screen.listen()
screen.onkey(fun=player.move, key="Up")

game_ended = False
while not game_ended:
    car.create_cars()
    time.sleep(0.1)
    screen.update()
    car.move_allcars()
    for each in car.all_cars:
        if player.distance(each) < PROXIMITY:
            score.game_over_write()
            game_ended = True
    if player.finish_line():
        player.reset_pos()
        car.MOVE_DISTANCE = 1.1*car.MOVE_DISTANCE
        score.LEVEL += 1
        score.score_update()


screen.exitonclick()
