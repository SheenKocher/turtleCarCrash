from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-220,270)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level : {self.level}", align="center",font= FONT)



    def increase_level(self):
        self.level +=1

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!",align="center",font=FONT)




