from turtle import Turtle, Screen

screen = Screen()
turtle = Turtle()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong Game")
turtle.shapesize(stretch_wid=5, stretch_len=1)
screen.tracer(0)
turtle.shape("square")
turtle.color("white")
turtle.penup()
turtle.goto(350, 0)


screen.listen()

def go_up():
    new_y = turtle.ycor() + 30
    turtle.goto(turtle.xcor(), new_y)

def go_down():
    new_y = turtle.ycor() - 30
    turtle.goto(turtle.xcor(), new_y)

screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()





screen.exitonclick()