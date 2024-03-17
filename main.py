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
    time.sleep(0.08)
    screen.update()
    ball.move()

    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()
    
    if ball.distance(r_paddle) <50 and ball.xcor() > 320:
        ball.bounce_x()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_position()
    if ball.xcor() < -380:
        ball.reset_position()






screen.exitonclick()