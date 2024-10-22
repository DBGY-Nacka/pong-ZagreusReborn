from turtle import Screen, textinput
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# din screen bör vara rektanguljär, ex. 800x600

screen = Screen()
screen.setup(801, 601)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
p1_name = ""
p2_name = ""
while p1_name == "":
    p1_name = textinput("Pong", "Name of the left player")
while p2_name == "":
    p2_name = textinput("Pong", "Name of the right player")

player1_keys = {"w": False, "s": False}
player2_keys = {"Up": False, "Down": False}

def p1_w():
    player1_keys["w"] = True
    
def p1_wr():
    player1_keys["w"] = False
    
def p1_s():
    player1_keys["s"] = True
    
def p1_sr():
    player1_keys["s"] = False
    
def p2_up():
    player2_keys["Up"] = True
    
def p2_upr():
    player2_keys["Up"] = False
    
def p2_down():
    player2_keys["Down"] = True
    
def p2_downr():
    player2_keys["Down"] = False

def main():
    game_length = 100
    game_is_on = True
    sudden_death = False
    
    p1 = Paddle(p1_name, (-375, 0))
    p2 = Paddle(p2_name, (370, 0))
    ball = Ball()
    scoreboard = Scoreboard(p1, p2)
    
    screen.listen()
    screen.onkeypress(p1_w, "w")
    screen.onkeyrelease(p1_wr, "w")
    screen.onkeypress(p2_up, "Up")
    screen.onkeyrelease(p2_upr, "Up")
    screen.onkeypress(p1_s, "s")
    screen.onkeyrelease(p1_sr, "s")
    screen.onkeypress(p2_down, "Down")
    screen.onkeyrelease(p2_downr, "Down")
    
    while game_is_on:
        
        screen.update()
        time.sleep(0.1)
        
        p1.move_up(player1_keys["w"])
        p2.move_up(player2_keys["Up"])
        p1.move_down(player1_keys["s"])
        p2.move_down(player2_keys["Down"])
        ball.move()
        
        if ball.ycor() > 290 or ball.ycor() < -290:
            ball.wall_bounce()
        
        if (ball.xcor() < p1.xcor() + 10 and
            ball.xcor() > p1.xcor() - 10 and
            ball.ycor() < p1.ycor() + 31 and 
            ball.ycor() > p1.ycor() - 31):
            ball.paddle_bounce("left")
        
        if (ball.xcor() > p2.xcor() - 10 and 
            ball.xcor() < p2.xcor() + 10 and 
            ball.ycor() < p2.ycor() + 31 and 
            ball.ycor() > p2.ycor() - 31):
            ball.paddle_bounce("right")
        
        if ball.xcor() > 390:
            scoreboard.increase_score(p1)
            ball.start(True)
        
        if ball.xcor() < -390:
            scoreboard.increase_score(p2)
            ball.start(False)

        if game_length <= 0:
            if p1.score == p2.score and sudden_death == False:
                scoreboard.sudden_death()
                sudden_death = True
                screen.update()
                time.sleep(5)
                scoreboard.clear()
                screen.update()
                
            elif p1.score > p2.score:
                screen.clear()
                scoreboard.game_over(p1, p2)
                screen.update()
                game_is_on = False
                
            elif p1.score < p2.score:
                screen.clear()
                scoreboard.game_over(p2, p1)
                screen.update()
                game_is_on = False
        
        if sudden_death == False:
            game_length -= 1
            scoreboard.update_time(game_length/10)
    screen.exitonclick()

if __name__ == "__main__":
    main()