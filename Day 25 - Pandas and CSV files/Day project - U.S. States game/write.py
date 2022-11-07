from turtle import Turtle

FONT = ("Courier", 14, "normal")


class Write(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.color("black")

    def write_state(self, x, y, user_answer):
        self.goto(x=x, y=y)
        self.write(f"{user_answer}", False, "center", font=FONT)

