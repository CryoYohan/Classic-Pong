from turtle import Turtle, Screen
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = Turtle()
        self.right_score = Turtle()
        self.center_net = Turtle()
        self.center_net.color('white')
        self.center_net.shape('square')
        self.center_net.shapesize(60, 1)


