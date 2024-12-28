from turtle import Turtle, Screen
from paddle import Paddle
from scoreboard import Scoreboard
class Window(Turtle):
    def __init__(self):
        super().__init__()
        # Initialize left and right paddles
        self.paddles_left = Paddle((-350,0))
        self.paddles_right = Paddle((350,0))

        # Initialize Scoreboard
        self.scoreboard = Scoreboard()

        # Setup window
        self.window = Screen()
        self.window.colormode(255)
        self.window.setup(800,600)
        self.window.bgcolor('black')
        self.window.title('Pong')
        self.window.tracer(0)

        # Listen Keys
        self.window.listen()
        # Left Paddle Controls
        self.window.onkeypress(self.paddles_left.go_up, 'w')
        self.window.onkeypress(self.paddles_left.go_down, 's')
        # Right Paddle Controls
        self.window.onkeypress(self.paddles_right.go_up, 'Up')
        self.window.onkeypress(self.paddles_right.go_down, 'Down')

        # Update Screen while game is running
        self.game_running = True
        while self.game_running:
            self.window.update()

        self.window.exitonclick()
        self.window.mainloop()

