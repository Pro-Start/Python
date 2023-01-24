# pomodoro


import math
import time
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TOTAL_REPS = 5
my_timer = None
mark = ""
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global mark
    global REPS
    window.after_cancel(my_timer)
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer, text="00:00")
    REPS = 0
    mark = ""
    check_label.config(text=mark)


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global REPS
    global TOTAL_REPS
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    REPS += 1
    if REPS > TOTAL_REPS:
        title_label.config(text="DONE!", fg=GREEN)
    elif REPS % TOTAL_REPS == 0:
        title_label.config(text="Last", fg=PINK)
        count_down(long_break_sec)
    elif REPS % 2 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(short_break_sec)
    elif REPS % 2 == 1:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def add_zero(number):
    if number < 10:
        number = "0" + str(number)
    return number


def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = round(count % 60)

    exact_time = str(add_zero(count_min)) + ":" + str(add_zero(count_sec))

    canvas.itemconfig(timer, text=exact_time)
    if count > 0:
        global my_timer
        count -= 1
        my_timer = window.after(1000, count_down, count)
    else:
        global mark
        start_timer()
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            mark += "✔️"
        check_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=FONT_NAME+", 50")
title_label.grid(column=2, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pic = PhotoImage(file="archive/028/tomato.png")
canvas.create_image(100, 112, image=pic)
timer = canvas.create_text(100, 130, text="00:00", fill="white",
                           font=(FONT_NAME, 25, "bold"))
canvas.grid(column=2, row=1)


start_button = Button(text="Start", command=start_timer)
start_button.grid(column=1, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=3, row=2)

check_label = Label(text="", fg=GREEN, bg=YELLOW)
check_label.grid(column=2, row=2)


window.mainloop()
