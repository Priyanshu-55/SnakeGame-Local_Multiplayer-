from turtle import Turtle


class Scoreboard(Turtle):
    
    def __init__(self,x_cor,y_cor,color):
        super().__init__()
        self.sc_color = color
        self.hideturtle()
        self.penup()
        self.goto(x_cor,y_cor)
        self.points = -1
        self.score()
        # self.x_cor = x_cor
        # self.y_cor = y_cor

    def score(self):
        self.clear()
        self.points += 1
        temp_score = "SCORE "+str(self.points)
        self.color(self.sc_color)
        self.write(temp_score,font=("Courier New",25,"bold"),align='center')