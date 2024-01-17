import smtplib
import datetime as dt
import random
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

def random_quote():
    with open("quotes.txt") as file:
        data = file.readlines()
        quotes = random.choice(data)
    return quotes

if today_date == 1:
    print("Send Email...")

   # send_email(text=quote)

else:
    print("Not Matched will send on Monday..")
