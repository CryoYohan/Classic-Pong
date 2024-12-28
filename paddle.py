from turtle import Turtle
class Paddle:
    def __init__(self, coordinates):
        # Initialize Paddle
        self.paddle = Turtle()
        self.paddle.penup()
        self.paddle.shape('square')
        self.paddle.color('white')
        self.paddle.goto(coordinates)
        self.paddle.shapesize(5, 1)

    # Control keys for the paddle
    def go_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def go_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)


