import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(height=600, width=800)
colors = ["black", "purple", "blue", "green", "yellow", "orange", "red", "pink"]
all_turtles = []
y_pos = 250
game_won = False


def draw_finish_line():
    finish_line = Turtle()
    finish_line.hideturtle()
    finish_line.penup()
    finish_line.setheading(90)
    finish_line.goto(x=350, y=-280)
    while finish_line.ycor() < 280:
        finish_line.pendown()
        finish_line.forward(10)
        finish_line.penup()
        finish_line.forward(10)


for i in range(8):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-350, y=y_pos)
    y_pos -= 70
    all_turtles.append(new_turtle)

draw_finish_line()
user_choice = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter the color: ")
while not game_won:
    for turtle in all_turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 350:
            winner = turtle
            game_won = True
            break


winner.goto(x=0, y=0)
if winner.color()[0] == user_choice:
    winner.write(f"YES! {winner.color()[0]} won.", font=('Arial', 20, 'bold'))
else:
    winner.write(f"No!! You lost. {winner.color()[0]} won.", font=('Arial', 20, 'bold'))
screen.exitonclick()