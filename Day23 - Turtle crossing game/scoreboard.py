from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.color("black")
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-290, y=270)
        self.write(f"LEVEL:{str(self.level)}", False, "Left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "Center", font=FONT)
