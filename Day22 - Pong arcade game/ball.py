from turtle import Turtle
import time
from random import randint


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        random = randint(0, 1)
        if random == 1:
            self.setheading(180)
        else:
            self.setheading(0)
    def restart(self):
        self.goto(x=0, y=0)
        self.screen.update()

