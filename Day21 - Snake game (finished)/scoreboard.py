from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.goto(x=0, y=275)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE:  {self.score}  HIGH SCORE: {self.high_score} ", False, ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write("GAME OVER", False, ALIGNMENT, font=FONT)

    def add_point(self):
        self.score += 1
        self.update_scoreboard()
