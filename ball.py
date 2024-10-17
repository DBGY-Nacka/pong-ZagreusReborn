from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.increase = 0
        self.shape("circle")
        self.speed(10 + self.increase)
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("white")
        self.start_direction = True
        self.start(True)
    
    def bounce(self):
        if self.start_direction == True:
            self.left(90)
        else:
            self.right(90)
        self.increase += 5
        
    def start(self, direction):
        self.increase = 0
        self.goto(0, 0)
        self.start_direction = direction
        if direction == True:
            self.setheading(45)
        else:
            self.setheading(225)