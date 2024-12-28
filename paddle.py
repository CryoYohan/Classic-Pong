from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, coordinates):
        # Initialize Paddle
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.goto(coordinates)
        self.shapesize(5, 1)

    # Control keys for the paddle
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


