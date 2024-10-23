from turtle import Turtle
from random import randint

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.increase = 0
        self.last_bounce = None
        self.shape("circle")
        self.movespeed = 6 + self.increase
        self.penup()
        self.shapesize(stretch_len = 1, stretch_wid = 1)
        self.color("white")
        self.start_direction = True
        self.mid_line()
        self.start(True)
    
    def mid_line(self):
        self.goto(0, 210)
        self.pendown()
        self.goto(0, -250)
        self.penup()
        self.goto(0, 0)
    
    def wall_bounce(self, sudden_death):
        self.setheading(-self.heading())
        self.increase += 0.5
        if sudden_death == True:
            self.increase += 1
        
    def paddle_bounce(self, paddle):
        if self.last_bounce != paddle:
            self.setheading(180 - self.heading() + randint(-20, 20))
            self.last_bounce = paddle
            if self.heading in range(70, 110) or self.heading in range(250, 290):
                if self.heading in range(70, 110):
                    if self.heading in range(70, 90):
                        self.setheading(70)
                    else:
                        self.setheading(110)
                else:
                    if self.heading in range(250, 270):
                        self.setheading(250)
                    else:
                        self.setheading(290)

    def move(self):
        self.forward(self.movespeed)

    def start(self, direction):
        self.increase = 0
        self.goto(0, 0)
        self.start_direction = direction
        if direction == True:
            if randint(1, 2) == 1:
                self.setheading(45)
            else:
                self.setheading(315)
        else:
            if randint(1, 2) == 1:
                self.setheading(135)
            else:
                self.setheading(225)