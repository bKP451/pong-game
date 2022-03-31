from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.goto(0, 0)
        self.dx = 10
        self.dy = 10
        self.move_speed = 0.1

    def move(self):
        x_new = self.xcor() + self.dx
        y_new = self.ycor() + self.dy
        self.goto(x_new, y_new)
        print(self.pos())

    def bounce_y(self):
        # print("I will bounce")
        self.dy *= -1
        self.move_speed *= 0.9
        # print(f"I am dy {self.dy}")

    def bounce_x(self):
        # print("hid the paddle")
        self.dx *= -1
        self.move_speed *= 0.9
        # print(f"I am dx {self.dx}")

    def change_turns(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        self.bounce_x()
