from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.goto(x=0, y=275)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write("SCORE: " + str(self.score), False, ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", False, ALIGNMENT, font=FONT)

    def add_point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()