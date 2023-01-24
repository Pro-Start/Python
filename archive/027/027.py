# tkinter-&-args-syntax

from tkinter import *

window = Tk()

window.title("GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# label
my_label = Label(text="im a label", font="Ariel, 20")
# my_label.place(x=200, y=0)
my_label.grid(column=1, row=1)

# input
my_input = Entry(width=20)
my_input.grid(column=2, row=2)


# spinbox
my_spinbox = Spinbox(from_=0, to=10, width=5)
my_spinbox.grid(column=2, row=3)


# button


def clicked():
    # txt1 = my_input.get()
    # my_label.config(text=txt1)
    txt2 = my_spinbox.get()
    my_label.config(text=txt2)


my_button = Button(text="Click here", command=clicked)
my_button.grid(column=4, row=4)

my_button2 = Button(text="Clicked")
my_button2.grid(column=3, row=1)


window.mainloop()


##################################################

def add(*args):
    sum = 0
    print(type(args))
    for item in args:
        sum += item
    print(sum)


def calculate(**kwargs):
    sum = 0
    print(type(kwargs))


add(1, 1, 10, 10)


calculate(add=3, multiply=3)


class Car:
    def __init__(self, **kw):
        self.model = kw.get('model')
        self.make = kw.get('make')


my_car = Car(make="Ford", model="Mustang")
print(my_car.make)
