import turtle
import time
import snake
from food import Food
from scoreboard import Scoreboard
import os
from playsound import playsound

# Set the current working directory to the location of the script
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# sounds
playsound('snake_bg.wav',block=False)


# Main Screen
main = turtle.Turtle()
turtle.setup(1.0,1.0)
# turtle.bgcolor('black')
turtle.bgpic("new_bg.png")
turtle.title("My First Snake Game")
turtle.tracer(0)

# snake of  first player
segments_lst_player1 = [[0,300],[-40,300],[-80,300]]
snake_1 = snake.Snake("blue",segments_lst_player1)
# key binding for first player
turtle.listen()
turtle.onkey(snake_1.up,'Up')
turtle.onkey(snake_1.down,'Down')
turtle.onkey(snake_1.right,'Right')
turtle.onkey(snake_1.left,'Left')
# Scoreboard for player one
scoreboard_one = Scoreboard(500,475,'blue')



# snake of  second player
segments_2nd_player2 = [[0,-300],[-40,-300],[-80,-300]]
snake_2 = snake.Snake("red",segments_2nd_player2)
# key binding for second player
turtle.listen()
turtle.onkey(snake_2.up,'w')
turtle.onkey(snake_2.down,'s')
turtle.onkey(snake_2.right,'d')
turtle.onkey(snake_2.left,'a')
# Scoreboard for player one
scoreboard_two = Scoreboard(-500,475,'red')


# Foods
no_of_foods = 15
foods = []
for i in range(no_of_foods):
    temp_food  =Food()
    foods.append(temp_food)


# Game over Text
def game_over():
    end_scrn = turtle.Turtle()
    end_scrn.hideturtle()
    end_scrn.color('yellow')
    end_scrn.write("Game Over ",font = ("Crucier New",50,"bold"),align='center')

    player_1_score =scoreboard_one.points
    player_2_score = scoreboard_two.points
    winner = "Both" if player_1_score == player_2_score else "Blue" if player_1_score > player_2_score else "Red"
    win_scrn=turtle.Turtle()
    win_scrn.penup()
    win_scrn.hideturtle()
    win_scrn.color('yellow')
    win_scrn.goto(0,200)
    win_scrn.write((winner+" Wins"),font = ("Crucier New",50,"bold"),align='center')


snake_1_live = True
snake_2_live = True
game_flag = True
delay = 0.15
while game_flag:
    turtle.update()
    time.sleep(delay)

    #distance method is used to compare the distance of object wrt to another object
    for food in foods:
        
        if snake_1.head.distance(food) < 45:
            food.sound()
            food.refresh()
            scoreboard_one.score()
            snake_1.extend()
        if snake_2.head.distance(food) < 45:
            food.sound()
            food.refresh()
            scoreboard_two.score()
            snake_2.extend()

# Wall collision detection  for snake1
    if snake_1.head.xcor() > 925 or snake_1.head.xcor() < -940 or snake_1.head.ycor() > 500 or snake_1.head.ycor() < -500:
        snake_1_live = False

# Wall collision detectioni for snake2
    if snake_2.head.xcor() > 925 or snake_2.head.xcor() < -940 or snake_2.head.ycor() > 500 or snake_2.head.ycor() < -500:
        snake_2_live = False

# Tail collision detection
# snake_1.segment{1:} so that it wont iterate the head becz head is < 10 always
    for segment in snake_1.segments[1:]:
        if snake_1.head.distance(segment) < 10:
            snake_1_live = False
# Tail collision with second snake detection
    for segment in snake_1.segments[1:]:
        if snake_2.head.distance(segment)<20:
            snake_2_live = False

# Tail collision detection for snake2
# snake_1.segment{1:} so that it wont iterate the head becz head is < 10 always
    for segment in snake_2.segments[1:]:
        if snake_2.head.distance(segment) < 10:
            snake_2_live = False    
# Tail collision with second snake detection
    for segment in snake_2.segments[1:]:
        if snake_1.head.distance(segment)<20:
            snake_1_live = False

    if snake_1_live:
        snake_1.move()
    if snake_2_live:
        snake_2.move()
    if not(snake_2_live) and not(snake_1_live):
        game_over()
        playsound("game_over_sound.mp3",block=False)
        time.sleep(2)
        turtle.bye()