import time
from turtle import Screen
from padel import Padel
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
right_padel = Padel(350)
left_padel = Padel(-350)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_padel.up, "Up")
screen.onkey(right_padel.down, "Down")
screen.onkey(left_padel.up, "w")
screen.onkey(left_padel.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

#     detect if hit wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if (ball.distance(right_padel) < 50 and ball.xcor() > 320) or (ball.distance(left_padel) < 50 and ball.xcor() < -320):
        ball.bounce_padel()

    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()
    #     Score for left
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()
#         score for right

screen.exitonclick()