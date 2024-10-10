from turtle import Turtle

class Paddle(Turtle):
    
    MOVE_DISTANCE = 10
    
    def __init__(self, position):
        id += 1
        super().__init__()
        self.body = []
        self.position = position
        self.initialize()
    
    def initialize(self):
        y = 0
        for _ in range(3):
            self.add_part(y)
            y -= 10
    
    def add_part(self, y):
        temp_turtle = Turtle(shape = "square")
        temp_turtle.color("white")
        temp_turtle.penup()
        temp_turtle.goto(self.position[0], self.position[1] - y)
        self.body.append(temp_turtle)
        
    def move(self, direction):
        if direction == True:
            self.setheading(90)
            for i in self.body:
                i.forward(self.MOVE_DISTANCE)
        else:
            self.setheading(270)
            for i in self.body:
                i.forward(self.MOVE_DISTANCE)