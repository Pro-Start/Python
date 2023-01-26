# email-random-quote

import smtplib
import datetime as dt
import random

# CONFIG
my_email = "thisispratikkabade@gmail.com"
my_password = "#############"
to_mail = "pratik.kabade@outlook.com"


# DATA
now = dt.datetime.now()
weekday = now.weekday()
days_text = ["Monday", "Tuesday", "Wednesday",
             "Thursday", "Friday", "Saturday", "Sunday"]
week_day = days_text[weekday - 1]


def send():
    with open("archive/032/data/quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        todays_quote = random.choice(all_quotes)
        print(todays_quote)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_mail,
                msg=f"Subject: {week_day} Motivation\n\n{todays_quote}"
            )

            btn.config(text="Send Again?")


window = Tk()
window.config(padx=100, pady=100)

txt = Label(text="ad", font="Ariel 40")
txt.grid(column=0, row=0)

btn = Button(text="Send Mail", command=send)
btn.grid(column=0, row=1)


window.mainloop()
