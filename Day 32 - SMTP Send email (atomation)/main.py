# import smtplib
#
# my_email = "hubert.smtp.test@gmail.com"
# password = "gcttfrotdomgzvev"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="karolina.smtp@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of my email"
#     )
#
#
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# print(year)
#
# date_of_birth = dt.datetime(year=2000, month=5, day=29)
#
# print(date_of_birth)

########## CHALLENGE 1 - SEND A MOTIVATIONAL QUOTE VIA EMAIL ON THE CURRENT WEEKDAY ###############
# import smtplib
# import datetime as dt
# import random
#
# MY_EMAIL = "hubert.smtp.test@gmail.com"
# PASSWORD = "gcttfrotdomgzvev"
#
# with open("quotes.txt", mode="r") as file:
#     all_quotes = file.readlines()
#     quote = random.choice(all_quotes)
#
# now = dt.datetime.now()
# todays_weekday = dt.datetime.weekday(now)
#
#
# if todays_weekday == 0:
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=MY_EMAIL, password=PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs="karolina.smtp@yahoo.com",
#             msg=f"Subject:Motivation Quote\n\n{quote}"
#         )
#

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv TICK

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import datetime as dt
import pandas as pd
import smtplib
import random

MY_EMAIL = "hubert.smtp.test@gmail.com"
PASSWORD = "gcttfrotdomgzvev"

# Read data from csv file
birthdays = pd.read_csv("birthdays.csv")

# Get today's date
todays_date = dt.datetime.now()
day = str(todays_date.day)
month = str(todays_date.month)
todays_day_month = day + month

#take first line of the letter in order to change "[NAME]" into birthday name
random_letter_ID = random.randint(1,3)
with open(f"letter_templates/letter_{random_letter_ID}.txt") as file:
    heading = file.readline()
    letter = file.read()


# for every person in birthday.csv file, check if birthday date matches today's date
for (index, row) in birthdays.iterrows():
    birthday_name = row["name"]
    birthday_day = str(row["day"])
    birthday_month = str(row["month"])
    birthday_email = row["email"]


    birthday_day_month = birthday_day + birthday_month
    if birthday_day_month == todays_day_month:
        name_heading = heading.replace("[NAME],", birthday_name + ",")
        message_content = name_heading + letter
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday_email,
                msg=f"Subject:Happy birthday {birthday_name}\n\n{message_content}"
            )

