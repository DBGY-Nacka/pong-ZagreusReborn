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
        
        
    def move_up(self, key_pressed):
        if self.ycor() < 280 and key_pressed == True:
            y = self.ycor()
            self.sety(y + self.MOVE_DISTANCE)
        
    def move_down(self, key_pressed):
        if self.ycor() > -280 and key_pressed == True:
            y = self.ycor()
            self.sety(y - self.MOVE_DISTANCE)