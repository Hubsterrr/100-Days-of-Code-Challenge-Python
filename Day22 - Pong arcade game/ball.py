from turtle import Turtle
import time
from random import randint


random_number = randint(0, 1)
if random_number == 0:
    heading = 0
else:
    heading = 180


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()

    def restart(self):
        self.goto(x=0, y=0)
        self.setheading(heading)
        self.screen.update()

