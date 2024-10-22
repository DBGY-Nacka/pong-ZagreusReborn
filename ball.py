from turtle import Turtle
from random import randint

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.increase = 0
        self.last_bounce = None
        self.shape("circle")
        self.movespeed = 10 + self.increase
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("white")
        self.start_direction = True
        self.start(True)
    
    def wall_bounce(self):
        self.setheading(-self.heading())
        self.increase += 5
        
    def paddle_bounce(self, paddle):
        if self.last_bounce != paddle:
            self.setheading(180 - self.heading() + randint(-20, 20))
            self.last_bounce = paddle

    def move(self):
        self.forward(self.movespeed)

    def start(self, direction):
        self.increase = 0
        self.goto(0, 0)
        self.start_direction = direction
        if direction == True:
            self.setheading(45)
        else:
            self.setheading(225)