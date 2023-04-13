from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.title("THE GREATEST PONG GAME")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    # detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with Right Paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    # detect collision with Left Paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


screen.exitonclick()
