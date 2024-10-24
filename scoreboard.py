from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 10, "normal")
FONT2 = ("Courier", 24, "normal")
POSITION = (0, 215)

class Scoreboard(Turtle):
    
    def __init__(self, p1, p2):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(POSITION)
        self.p1 = p1
        self.p2 = p2
        self.update_scoreboard(p1, p2)
        self.hideturtle()
        
    def update_scoreboard(self, p1, p2):
        self.write(f"{p1.name}: {p1.score} SCORE {p2.name}: {p2.score}",
                   align = ALIGNMENT, font = FONT)
    
    def update_time(self, time):
        self.clear()
        self.goto(0, 230)
        self.write(f"Time remaining: {time:0.1f}",
                   align = ALIGNMENT, font = FONT)
        self.goto(POSITION)
        self.update_scoreboard(self.p1, self.p2)
    
    def game_over(self, winner, loser):
        self.goto(0, 0)
        text = ("Game completed " 
        + str(winner.name) 
        + " wins over " 
        + str(loser.name)
        + " with "
        + str(winner.score) 
        + " score versus "
        + str(loser.score)
        + " score")
        self.write(text, align = ALIGNMENT, font = FONT)
    
    def increase_score(self, paddle):
        paddle.score += 1
        self.clear()
        self.update_scoreboard(self.p1, self.p2)
    
    def sudden_death(self):
        self.clear()
        self.goto(0, 0)
        self.write("Sudden Death", align = ALIGNMENT, font = FONT2)