# password-generator

from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
    alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                 "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    capital_alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                         "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    password_list = []

    tot_numbers = random.randint(2, 4)
    tot_symbols = random.randint(2, 4)
    tot_alphabets = random.randint(4, 8)
    tot_capital_alphabets = random.randint(2, 4)

    for char in range(tot_numbers):
        password_list += random.choice(numbers)

    for char in range(tot_symbols):
        password_list += random.choice(symbols)

    for char in range(tot_alphabets):
        password_list += random.choice(alphabets)

    for char in range(tot_capital_alphabets):
        password_list += random.choice(capital_alphabets)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please fill the details")

    else:
        is_ok = messagebox.showinfo(title="Save Password?",
                                    message=f"Details you've entered: \nEmail: {email} \nPassword: {password} \nIs this OK?")

        if is_ok:
            with open("archive/029/passwords.txt", "a") as local_file:
                local_file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=10, pady=10)

canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(file="archive/029/logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# ---------------------------- LABELS
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

password_label = Label(text='Password')
password_label.grid(column=0, row=3)


# ---------------------------- ENTRIES
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "pratik.kabade@outlook.com")


password_input = Entry(width=21)
password_input.grid(column=1, row=3)


# ---------------------------- BUTTONS
generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
