from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.q_num = 0

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(
            text="Score: 0", fg="white", bg=THEME_COLOR, font="Ariel, 20")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = PhotoImage(file="archive/034/images/true.png")
        self.true_button = Button(
            image=true_image, highlightthickness=0, command=self.true_press)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="archive/034/images/false.png")
        self.false_button = Button(
            image=false_image, highlightthickness=0, command=self.false_press)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.q_num < 10:
            self.canvas.config(bg="white")
            self.q_num += 1
            self.score_label.config(
                text=f"Score: {self.quiz.score}/{self.q_num}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text="GAME OVER!")

    def true_press(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_press(self):
        is_right = self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)