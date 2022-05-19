from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard
import time


myscreen = Screen()
myscreen.setup(height=600, width= 800)
myscreen.bgcolor("black")
myscreen.title("Pong")
myscreen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = ScoreBoard()



myscreen.listen()
myscreen.onkey(r_paddle.go_up ,"Up")
myscreen.onkey(r_paddle.go_down ,"Down")
myscreen.onkey(l_paddle.go_up ,"w")
myscreen.onkey(l_paddle.go_down ,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    myscreen.update()
    ball.move()

    #detect collision with the top wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()

    #detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        

    #when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()







myscreen.exitonclick()