from turtle import Turtle,Screen
import random
import colors
from playsound import playsound


screen = Screen()
food_shape = ['circle','triangle','square']

#Food class now inherits the turtle class and behaving like an turtle object
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(random.choice(food_shape))
        self.penup()
        self.shapesize(2)
        self.speed('fastest')
        self.color('red')
        self.refresh()
    def refresh(self):
        x_cor = random.randint(-900,900)
        y_cor = random.randint(-450,450)
        self.goto(x_cor,y_cor)
        self.color(colors.rand_color())
        self.shape(random.choice(food_shape))
    
    def sound(self):
        playsound("food_eating_sound.mp3",block=False)
        