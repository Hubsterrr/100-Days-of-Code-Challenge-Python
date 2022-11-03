from paddle import Paddle
from ball import Ball
from turtle import Screen
from hud import Hud
import time

screen = Screen()
screen.setup(width=1920, height=1080)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

right = Paddle((930, 0))
left = Paddle((-930, 0))

hud = Hud()
ball = Ball()

# Key listener
answer = int(screen.numinput("CHOOSE GAME MODE", "SINGLE PLAYER: 1      MULTIPLAYER: 2", 1, 1, 2))
screen.listen()
if answer == 2:
    screen.onkey(left.up, "w")
    screen.onkey(left.down, "s")
screen.onkey(right.up, "Up")
screen.onkey(right.down, "Down")

# Game loop
game_is_on = True
while game_is_on:
    no_score = True
    time.sleep(0.5)

    while no_score:
        ball.move()
        screen.update()

        if answer == 1:
            left.move()

        # Detect collision with left and right paddle
        if ball.xcor() >= 910 and right.distance(ball) <= 80 or ball.xcor() <= 910 and left.distance(ball) <= 80:
            ball.bounce_x()
            ball.bounce_paddle()

        # Detect collision with top or bottom wall
        if ball.ycor() > 530 or ball.ycor() < -530:
            ball.bounce_y()

        # Detect collision with side walls
        if ball.xcor() > 960:
            hud.right_score += 1
            hud.update_scoreboard()
            ball.restart()
            no_score = False

        if ball.xcor() < -960:
            hud.left_score += 1
            hud.update_scoreboard()
            ball.restart()
            no_score = False


screen.exitonclick()
