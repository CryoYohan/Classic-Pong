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
        while self.game_running:
            try:
                sleep(self.ball.move_speed)
            except ValueError:
                print('Move speed value turns negative.')
                self.ball.reset_position()

            self.window.update()

            # Move ball
            self.ball.move()
            # Detect wall collisions then ball bounce
            if self.ball.ycor() > 280 or self.ball.ycor() < -280:
                self.ball.bounce_y()

            # Detect paddle right and left
            if self.ball.distance(self.paddles_right) < 50 and self.ball.xcor() > 320 or self.ball.distance(self.paddles_left) < 50 and self.ball.xcor() < -320:
                self.ball.bounce_x()

            # Detect ball out of bounds RIGHT and sets ball coordinates to center (0,0)
            if self.ball.xcor() > 380:
                self.scoreboard.l_point()
                self.scoreboard.update_scoreboard()
                self.ball.reset_position()

            # Detect ball out of bounds LEFT and sets ball coordinates to center (0,0)
            if self.ball.xcor() < -380:
                self.scoreboard.r_point()
                self.scoreboard.update_scoreboard()
                self.ball.reset_position()

        self.window.exitonclick()
        self.window.mainloop()

