from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(0)
        self.x_move = 5
        self.y_move = 5

    def restart(self):
        self.goto(x=0, y=0)
        self.x_move = 5
        self.y_move = 5
        self.bounce_x()
        self.screen.update()
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def bounce_paddle(self):
        if self.x_move < 0:
            self.x_move -= 1
        else:
            self.x_move += 1