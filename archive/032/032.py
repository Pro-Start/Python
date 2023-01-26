# birthday-email

import smtplib
import datetime as dt
import random
import pandas as pd
from tkinter import *

# --------------------- CONFIG ------------------------------------------ #
MY_EMAIL = "thisispratikkabade@gmail.com"
MY_PASSWORD = "##############"
MY_SMTP = "smtp.gmail.com"
# TO_MAIL = "pratik.kabade@outlook.com"


# --------------------- DATE --------------------------------------------- #

today = dt.datetime.now()
today_tuple = (today.month, today.day)


# ---------------------      --------------------------------------------- #
data = pd.read_csv("archive/032/data/birthdays.csv")

# birthdays_dict = {new_value: new_value for (index, data_row) in data.iterrows()}
birthdays_dict = {(data_row["month"], data_row["day"])                  : data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"archive/032/data/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP(MY_SMTP) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"], msg=f"Suject:Happy Birthday\n\n{contents}")
