from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
turtle = Turtle()

screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.title("Ping Pong Game")
screen.tracer(0)

ball = Ball()
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()





screen.exitonclick()