from turtle import Turtle, Screen
from paddle import Paddle
class Window(Turtle):
    def __init__(self):
        super().__init__()
        self.paddles = Paddle()
        self.net = Turtle()
        self.net.hideturtle()
        self.net.speed('fastest')
        self.net.pensize(10)
        self.net.color('white')
        self.net.pencolor('white')
        self.window = Screen()
        self.window.colormode(255)
        self.window.setup(800,600)
        self.window.bgcolor('black')
        self.window.exitonclick()
        self.window.mainloop()

    def draw_net(self):
        self.net.penup()
        self.net.goto(0,-300)
        self.net.pendown()
        self.net.left(90)
        for _ in range(15):
            self.net.penup()
            self.net.forward(20)
            self.net.pendown()
            self.net.forward(20)
        print(self.net.position())


