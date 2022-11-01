from turtle import Screen, Turtle
from snake import Snake
import time

# Window setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# snake = []
# starting_position = [(0, 0), (-20, 0), (-40, 0)]
#
# for position in starting_position:
#     snake_piece = Turtle("square")
#     snake_piece.color("white")
#     snake_piece.penup()
#     snake_piece.goto(position)
#     snake.append(snake_piece)




snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
