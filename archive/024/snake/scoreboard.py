from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
SCORE_LOCATION = (10, 270)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        saved_score = open("archive/024/snake/scoreboard.txt", mode="r")
        a = saved_score.read()
        seperator = a.find(',')
        saved_HIGH = a[:seperator]
        saved_NAME = a[seperator+1:]
        self.highscore = int(saved_HIGH)
        self.highscorer = saved_NAME
        saved_score.close()

        self.lives = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(SCORE_LOCATION)
        self.update_scoreboard()

    def set_name(self, inp):
        self.name = inp

    def update_scoreboard(self):
        self.write(
            f"Score: {self.score}. Highscore: {self.highscore}, Lives: {self.lives}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.highscorer = self.name
        self.score = 0
        self.lives += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(
            f"GAMEOVER! \nScore: {self.score}. \nHighscore: {self.highscore}, by {self.highscorer}",
            align=ALIGNMENT, font=FONT)

        save_score = open("archive/024/snake/scoreboard.txt", mode="w")
        command = save_score.write(
            str(self.highscore)+str(",")+str(self.highscorer))
