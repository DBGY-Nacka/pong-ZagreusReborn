from turtle import Turtle

class Paddle(Turtle):
    
    MOVE_DISTANCE = 10
    
    def __init__(self, name, position):
        super().__init__()
        self.score = 0
        self.name : str = name
        self.shapesize(stretch_len = 3, stretch_wid = 0.5)
        self.position = position
        self.shape("square")
        self.penup()
        self.setheading(90)
        self.color("white")
        self.goto(self.position[0], self.position[1])
        
        
    def move_up(self):
        if self.ycor() < 280 or self.ycor() > -280:
            pass
        else:
            self.setheading(90)
            self.forward(self.MOVE_DISTANCE)
        
    def move_down(self):
        if self.ycor() < 280 or self.ycor() > -280:
            pass
        else:
            self.setheading(270)
            self.forward(self.MOVE_DISTANCE)