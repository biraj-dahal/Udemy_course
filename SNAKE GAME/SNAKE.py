from turtle import Turtle
EASY_LEVEL = 20


class SNAKE:
    def __init__(self):
        self.snake_block = []
        self.make_snake()
        self.head = self.snake_block[0]

    def make_snake(self):
        x_pos = 0
        for i in range(3):
            square = Turtle(shape='square')
            square.penup()
            square.color('white')
            square.goto(x=x_pos, y=0)
            x_pos -= 20

            self.snake_block.append(square)

    def move(self):
        for block_num in range(len(self.snake_block) - 1, 0, -1):
            move_x = self.snake_block[block_num - 1].xcor()
            move_y = self.snake_block[block_num - 1].ycor()
            self.snake_block[block_num].goto(move_x, move_y)
        self.snake_block[0].forward(EASY_LEVEL)

    def change_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def change_down(self):
        if self.head.heading() != 90:
            self.head. setheading(270)

    def change_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def change_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def extend(self):
        square = Turtle(shape='square')
        square.penup()
        square.color('white')
        square.goto(self.snake_block[-1].position())
        self.snake_block.append(square)

