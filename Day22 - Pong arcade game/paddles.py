from turtle import Turtle


MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT_SIDE = -830
RIGHT_SIDE = 830
PLAYER_POSITION = [(LEFT_SIDE, -60), (LEFT_SIDE, -40), (LEFT_SIDE, -20),
                     (LEFT_SIDE, 0),
                     (LEFT_SIDE, 20), (LEFT_SIDE, 40), (LEFT_SIDE, 60)]

BOT_POSITION = [(RIGHT_SIDE, -60), (RIGHT_SIDE, -40), (RIGHT_SIDE, -20),
                     (RIGHT_SIDE, 0),
                     (RIGHT_SIDE, 20), (RIGHT_SIDE, 40), (RIGHT_SIDE, 60)]

PLAYER_TOP_POSITION = [(LEFT_SIDE, 400), (LEFT_SIDE, 420), (LEFT_SIDE, 440),
                (LEFT_SIDE, 460),
                (LEFT_SIDE, 480), (LEFT_SIDE, 500), (LEFT_SIDE, 520)]

PLAYER_BOTTOM_POSITION = [(LEFT_SIDE, -520), (LEFT_SIDE, -500), (LEFT_SIDE, -480),
                   (LEFT_SIDE, -460),
                   (LEFT_SIDE, -440), (LEFT_SIDE, -420), (LEFT_SIDE, -400)]


BOT_TOP_POSITION = [(RIGHT_SIDE, 400), (RIGHT_SIDE, 420), (RIGHT_SIDE, 440),
                (RIGHT_SIDE, 460),
                (RIGHT_SIDE, 480), (RIGHT_SIDE, 500), (RIGHT_SIDE, 520)]

BOT_BOTTOM_POSITION = [(RIGHT_SIDE, -520), (RIGHT_SIDE, -500), (RIGHT_SIDE, -480),
                   (RIGHT_SIDE, -460),
                   (RIGHT_SIDE, -440), (RIGHT_SIDE, -420), (RIGHT_SIDE, -400)]


class Paddles(Turtle):

    def __init__(self, player_or_bot):
        super().__init__()
        self.paddle = []
        if player_or_bot == "player":
            self.create_paddle(PLAYER_POSITION)
        else:
            self.create_paddle(BOT_POSITION)
        self.center = self.paddle[3]

    def create_paddle(self, coordinates_list):
        for position in coordinates_list:
            self.add_segment(position)

    def add_segment(self, position):
        paddle_piece = Turtle("square")
        paddle_piece.color("white")
        paddle_piece.penup()
        paddle_piece.goto(position)
        paddle_piece.setheading(UP)
        self.paddle.append(paddle_piece)

    def up(self):
        if self.paddle[-1].ycor() > 540:
            for chunk in range(0, len(self.paddle)):
                self.paddle[chunk].goto(PLAYER_TOP_POSITION[chunk])
        else:
            for chunk in self.paddle:
                chunk.setheading(UP)
                chunk.forward(30)

    def down(self):
        if self.paddle[0].ycor() < -540:
            for chunk in range(0, len(self.paddle)):
                self.paddle[chunk].goto(PLAYER_BOTTOM_POSITION[chunk])
        else:
            for chunk in self.paddle:
                chunk.setheading(DOWN)
                chunk.forward(30)

    def move(self):
        for chunk in self.paddle:
            chunk.forward(20)
        if self.paddle[0].ycor() < -540:
            for chunk in range(0, len(self.paddle)):
                self.paddle[chunk].goto(BOT_BOTTOM_POSITION[chunk])
                self.paddle[chunk].setheading(UP)
                self.paddle[chunk].forward(15)
        elif self.paddle[-1].ycor() > 540:
            for chunk in range(0, len(self.paddle)):
                self.paddle[chunk].goto(BOT_TOP_POSITION[chunk])
                self.paddle[chunk].setheading(DOWN)
                self.paddle[chunk].forward(15)



 # counter = 0
        # for chunk in self.paddle:
        #     if chunk.ycor() < -540:
        #         chunk.goto(BOT_BOTTOM_POSITION[counter])
        #         chunk.setheading(UP)
        #         chunk.forward(20)
        #         counter += 1
        #
        #     chunk.setheading(DOWN)
        #     chunk.forward(20)