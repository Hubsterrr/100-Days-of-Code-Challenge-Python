from hud import Hud
from paddles import Paddles
from ball import Ball
from turtle import Screen
import time

RIGHT = 0
RIGHT_UP = 45
UP = 90
LEFT_UP = 135
LEFT = 180
LEFT_DOWN = 225
DOWN = 270
RIGHT_DOWN = 315


screen = Screen()
screen.setup(width=1820, height=980)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

hud = Hud()

player_paddle = Paddles("player")
bot_paddle = Paddles("bot")
ball = Ball()

# Key listener
screen.listen()
screen.onkey(player_paddle.up, "Up")
screen.onkey(player_paddle.down, "Down")

# Game loop
game_is_on = True
while game_is_on:

    ball.restart()
    no_score = True
    time.sleep(0.5)
    while no_score:
        screen.update()

        ball.forward(5)

        bot_paddle.move()

        # Detect collision with Player paddle
        player_paddle_angle = -45
        for chunk in player_paddle.paddle:
            if chunk.distance(ball) <= 15:
                ball.setheading(player_paddle_angle)
            player_paddle_angle += 15

        # Detect collision with Bot paddle
        bot_paddle_angle = 225
        for chunk in bot_paddle.paddle:
            if chunk.distance(ball) <= 15:
                ball.setheading(bot_paddle_angle)
            bot_paddle_angle += -15

        # Detect collision with top or bottom wall
        if ball.ycor() > 510 or ball.ycor() < -510:
            angle = ball.heading()
            ball.setheading(angle + 90)

        #Detect collision with side walls
        if ball.xcor() > 950:
            hud.player_score += 1
            hud.update_scoreboard()
            no_score = False

        elif ball.xcor() < -950:
            hud.bot_score += 1
            hud.update_scoreboard()
            no_score = False


screen.exitonclick()
