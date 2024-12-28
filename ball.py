from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.pensize(30)
        self.x = 10
        self.y = 10

    def move(self):
        new_y = self.ycor() + self.y
        new_x = self.xcor() + self.x
        self.goto(new_x,new_y)

    def bounce(self):
        self.y *= -1
    def hit(self):
        self.x *= -1

