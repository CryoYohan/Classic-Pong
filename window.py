from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep
class Window(Turtle):
    def __init__(self):
        super().__init__()
        # Setup window
        self.window = Screen()
        self.window.tracer(0)
        self.window.colormode(255)
        self.window.setup(800,600)
        self.window.bgcolor('black')
        self.window.title('Pong')

        # Initialize left and right paddles
        self.paddles_left = Paddle((-350, 0))
        self.paddles_right = Paddle((350, 0))

        # Initialize Scoreboard
        self.scoreboard = Scoreboard()

        # Initialize Ball
        self.ball = Ball()

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
        self.x = 10
        self.y = 10
        while self.game_running:
            sleep(0.1)
            self.window.update()
            self.ball.move(x=self.x,y=self.y)
            if self.ball.ycor() == 280:
                self.y = -10
                self.ball.move(x=self.x,y=self.y)
            elif self.ball.ycor() == -280:
                self.y = 10
                self.ball.move(x=self.x,y=self.y)
            elif self.ball.xcor() == 380:
                self.x = -10
                self.ball.move(x=self.x,y=self.y)
            elif self.ball.xcor() == -380:
                self.x = 10
                self.ball.move(x=self.x,y=self.y)
            print(self.ball.xcor(),self.ball.ycor())


        self.window.exitonclick()
        self.window.mainloop()

