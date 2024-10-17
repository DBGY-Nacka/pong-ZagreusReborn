from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# din screen bör vara rektanguljär, ex. 800x600

#p1_name = input("What is the name of player 1: ")
#p2_name = input("What is the name of player 2: ")

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

def main():
    
    game_is_on = True
    
    p1 = Paddle("p1_name", (-375, 0))
    p2 = Paddle("p2_name", (370, 0))
    
    screen.listen()
    screen.onkey(p1.move_up, "w")
    screen.onkey(p2.move_up, "Up")
    screen.onkey(p1.move_down, "s")
    screen.onkey(p2.move_down, "Down")
    
    while game_is_on:
        
        screen.update()
        time.sleep(0.1)
        
        
    
    screen.exitonclick()

if __name__ == "__main__":
    main()