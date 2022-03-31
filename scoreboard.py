from turtle import Turtle
FONT = ('Courier', 60, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.left_score = 0
        self.right_score = 0
        self.score_updates()

    def score_updates(self):
        self.goto(-100, 200)
        self.clear()
        self.write(self.left_score, align='center', font=FONT)
        self.goto(100, 200)
        self.write(self.right_score, align='center', font=FONT)

    def right_got_point(self):
        self.right_score += 1
        self.score_updates()

    def left_got_point(self):
        self.left_score += 1
        self.score_updates()


