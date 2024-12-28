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

        self.window.exitonclick()
        self.window.mainloop()
