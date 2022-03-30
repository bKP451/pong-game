from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
window = Screen()
window.setup(width=800, height=600)
window.bgcolor('black')
window.title("PONG")
window.tracer(0)
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
game_ball = Ball()

game_is_on = True
window.listen()
window.onkey(fun=right_paddle.up, key="Up")  # parentheses must be omitted when using functions as parameters
window.onkey(fun=right_paddle.down, key="Down")
window.onkey(fun=left_paddle.up, key="w")
window.onkey(fun=left_paddle.down, key="s")
while game_is_on:
    time.sleep(0.2)
    window.update()
    if game_ball.ycor() < -300:
        print("OH I hit the bottom wall !!")
        game_ball.bounce()
    game_ball.move()

window.exitonclick()