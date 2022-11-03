from turtle import Turtle

MOVE_DISTANCE = 60
UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(1, 7)
        self.setheading(90)
        self.goto(position)

    def up(self):
        if self.ycor() > 440:
            self.sety(470)
        else:
            self.setheading(UP)
            self.forward(MOVE_DISTANCE)

    def down(self):
        if self.ycor() < -440:
            self.sety(-470)
        else:
            self.setheading(DOWN)
            self.forward(MOVE_DISTANCE)

    def move(self):
        self.forward(20)
        if self.ycor() < -440:
            self.sety(-470)
            self.setheading(UP)
            self.forward(20)
        elif self.ycor() > 440:
            self.sety(470)
            self.setheading(DOWN)
            self.forward(20)
