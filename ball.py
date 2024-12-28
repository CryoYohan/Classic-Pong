from turtle import Turtle
from random import randint
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.pensize(30)

    def move(self,**kwargs):
        new_y = self.ycor() + kwargs.get('y')
        new_x = self.xcor() + kwargs.get('x')
        self.goto(new_x,new_y)

    def bounce(self):
        pass