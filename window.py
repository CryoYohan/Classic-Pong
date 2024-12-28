from turtle import Turtle, Screen
from paddle import Paddle
from scoreboard import Scoreboard
class Window(Turtle):
    def __init__(self):
        super().__init__()
        # Initialize modules
        self.paddles = Paddle()
        self.scoreboard = Scoreboard()
        self.window = Screen()
        # Setup window
        self.window.colormode(255)
        self.window.setup(800,600)
        self.window.bgcolor('black')
        self.window.title('Pong')

        # Listen Keys
        self.window.listen()

        self.window.onkey(self.paddles.go_up_left, 'w')
        self.window.onkey(self.paddles.go_down_left, 's')

        self.window.onkey(self.paddles.go_up_right, 'Up')
        self.window.onkey(self.paddles.go_down_right, 'Down')

        self.window.exitonclick()
        self.window.mainloop()
