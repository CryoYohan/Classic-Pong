from turtle import Turtle
class Paddle:
    def __init__(self):
        # Initialize Variables
        self.WIDTH = 20
        self.HEIGHT = 100
        self.LEFT_XCOR = 350
        self.RIGHT_XCOR = -350
        self.YCOR = 0
        # Initialize left and right turtle paddles
        self.left = Turtle()
        self.right = Turtle()
        self.left.shape('square')
        self.right.shape('square')
        self.left_paddle()
        self.right_paddle()

    # Create the two paddles, left and right

    def right_paddle(self):
        self.right.penup()
        self.right.setx(self.RIGHT_XCOR)
        self.right.sety(self.YCOR)
        self.right.shapesize(5, 1)
        self.right.color('white')

    def left_paddle(self):
        self.left.penup()
        self.left.setx(self.LEFT_XCOR)
        self.left.sety(self.YCOR)
        self.left.shapesize(5, 1)
        self.left.color('white')

    # Control keys for the left and right paddles
    def go_up(self):
        self.left.setx(self.YCOR + 10)

    def go_down(self):
        self.left.setx(self.YCOR - 10)




