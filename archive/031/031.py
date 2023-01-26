# flash-card

from tkinter import *
import pandas as pd
import random
# ---------------------------- COLOURS ------------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- DATA ---------------------------------------- #

try:
    data_file = pd.read_csv("archive/031/data/unknown_words.csv")
except FileNotFoundError:
    data_file = pd.read_csv("archive/031/data/french_words.csv")
    print("New DATA generated")
df = data_file.to_dict('records')
current_number = 0
next_image_timer = 3000

# ---------------------------- FUNCTIONS ----------------------------------- #


def text_card():
    global current_number, next_image_timer
    window.after_cancel(next_image_timer)
    canvas.itemconfig(card_background, image=card_front_image)

    random_number = random.randint(0, len(df))
    current_number = random_number

    random_french_word = df[random_number]["French"]

    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=random_french_word, fill="black")

    next_image_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_background, image=card_back_image)

    random_english_word = df[current_number]["English"]

    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=random_english_word, fill="white")


def is_known():
    df.remove(df[current_number])

    new_file = pd.DataFrame(df)
    new_file.to_csv("archive/031/data/unknown_words.csv")
    print(len(new_file))
    text_card()


# ---------------------------- UI ------------------------------------------ #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="archive/031/images/card_front.png")
card_back_image = PhotoImage(file="archive/031/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

language = canvas.create_text(
    400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 68, "bold"))

canvas.grid(row=0, column=0, columnspan=2)


# ---------------------------- BUTTONS ------------------------------------- #
cross_image = PhotoImage(file="archive/031/images/wrong.png")
unknown_button = Button(
    image=cross_image, highlightthickness=0, command=flip_card)
unknown_button.grid(row=1, column=0)

correct_image = PhotoImage(file="archive/031/images/right.png")
done_button = Button(image=correct_image,
                     highlightthickness=0, command=is_known)
done_button.grid(row=1, column=1)

text_card()

window.mainloop()
