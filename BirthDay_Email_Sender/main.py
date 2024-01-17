##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import smtplib
import datetime as dt
import random

import pandas

my_email = "ganga4cs@gmail.com"
password = "juxsvttgeswvcnih"


date = dt.datetime.now()
today_date = date.weekday()
print(type(today_date))


def send_email(text):
    connection = smtplib.SMTP("smtp.gmail.com")
    print("Sending Email..")
    connection.starttls()  # Securing our Email data Make our connection secure using this method
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="gangadharbsk@gmail.com",
                        msg=f"Subject:HelloGangadhar\n\n{text}.")
    print("Email Sent done")
    connection.close()


data = pandas.read_csv("birthdays.csv")
print(data['email'])




