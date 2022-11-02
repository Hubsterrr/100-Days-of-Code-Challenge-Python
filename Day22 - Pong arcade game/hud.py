from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 100, "bold")


class Hud(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.draw_center()
        self.player_score = 0
        self.bot_score = 0
        self.update_scoreboard()

    def draw_center(self):
        self.pensize(10)
        self.goto(x=0, y=-550)
        self.setheading(90)
        for _ in range(35):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(25)

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-100, y=440)
        self.write(str(self.player_score), False, ALIGNMENT, font=FONT)
        self.goto(x=100, y=440)
        self.write(str(self.bot_score), False, ALIGNMENT, font=FONT)
        self.draw_center()


