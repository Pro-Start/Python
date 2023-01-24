# mile-to-km

from tkinter import *

window = Tk()
window.title("Mile to KM converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)


t1 = Label(text="Miles", font="Ariel, 15")
t2 = Label(text="Km", font="Ariel, 15")
t3 = Label(text="equals", font="Ariel, 13")

t1.grid(column=3, row=1)
t2.grid(column=3, row=2)
t3.grid(column=1, row=2)


def clicked():
    miles = round(int(inp.get()) * 1.689)
    val.config(text=miles)


inp = Entry(width=15)
val = Label(text="0", font="Ariel, 15")
btn = Button(text="Click here", command=clicked)

inp.grid(column=2, row=1)
val.grid(column=2, row=2)
btn.grid(column=2, row=3)


window.mainloop()
