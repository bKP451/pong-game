from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
window = Screen()
window.setup(width=800, height=600, startx=700)
window.bgcolor('black')
window.title("PONG")
window.tracer(0)
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
game_ball = Ball()
scoreboard = Scoreboard()
game_is_on = True
window.listen()
window.onkey(fun=right_paddle.up, key="Up")  # parentheses must be omitted when using functions as parameters
window.onkey(fun=right_paddle.down, key="Down")
window.onkey(fun=left_paddle.up, key="w")
window.onkey(fun=left_paddle.down, key="s")
while game_is_on:
    time.sleep(game_ball.move_speed)
    window.update()

    # Collision with the walls(top and bottom)
    if game_ball.ycor() < -280 or game_ball.ycor() > 280:
        game_ball.bounce_y()
        print("OH I hit the bottom wall !!")

    if game_ball.distance(right_paddle) < 50 and game_ball.xcor() > 320 or game_ball.distance(left_paddle) < 50 \
            and game_ball.xcor() < -320:
        # y coordinates is already in the decreasing order because it has already collided with the wall
        game_ball.bounce_x()

    # Pointing out right paddle miss
    if game_ball.xcor() > 350:
        game_ball.change_turns()
        scoreboard.left_got_point()

    # Pointing out left paddle miss
    if game_ball.xcor() < -350:
        game_ball.change_turns()
        scoreboard.right_got_point()

    game_ball.move()

window.exitonclick()
