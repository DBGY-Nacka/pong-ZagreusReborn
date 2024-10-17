from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")
POSITION = (0, 265)

class Scoreboard(Turtle):
    
    def __init__(self, p1, p2):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(POSITION)
        self.update_scoreboard(p1, p2)
        self.hideturtle()
        
    def update_scoreboard(self, p1, p2):
        self.write(f"{p1.name}: {p1.score} SCORE {p2.name}: {p2.score}", align = ALIGNMENT, font = FONT)
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align = ALIGNMENT, font = FONT)
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()