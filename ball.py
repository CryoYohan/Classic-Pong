from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.pensize(30)
        self.x = 10
        self.y = 10
        self.move_speed = 0.1
    # Moves the ball adding 10 pixels every iteration
    def move(self):
        new_y = self.ycor() + self.y
        new_x = self.xcor() + self.x
        self.goto(new_x,new_y)
    # Bounce top and bottom
    def bounce_y(self):
        self.y *= -1
    # Bounce left and right
    def bounce_x(self):
        self.x *= -1
        self.move_speed -= 0.01  # Increases the movement speed of ball

    # Reset ball position to center coordinates (0,0)
    def reset_position(self):
        self.move_speed = 0.1  # Reset ball speed
        self.home()
        self.bounce_x()  # Flips the ball's direction to avoid bias on serve ball


