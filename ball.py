from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)

    def move(self):
        x_new = self.xcor() - 10
        y_new = self.ycor() - 10
        self.goto(x_new, y_new)
        print(self.pos())