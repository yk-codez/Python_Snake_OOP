
from turtle import Turtle 

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()

        self.score = 0
        self.color('White')
        self.penup()
        self.goto(0, 270)
        self.write(f'Score: {self.score}', align='center', font=('arial', 25, 'normal'))
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f'Score: {self.score}', align='center', font=('arial', 25, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER', align='center', font=('arial', 30, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        