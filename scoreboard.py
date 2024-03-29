from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("my_file.txt") as data:
            self.high_score=int(data.read())

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def reset_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("my_file.txt", mode='w') as  data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.update_scoreboard()
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER .", align="center", font=("Arial", 24, "normal"))
        self.color("white")

    def increase_score(self):
        self.clear()
        self.score += 1
        self.clear()
        self.update_scoreboard()