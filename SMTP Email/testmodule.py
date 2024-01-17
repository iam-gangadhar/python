import datetime as dt
date = dt.datetime.now()
print(date)
print(date.year)
print(date.month)
print(date.weekday())
birthday = dt.datetime(year=1989, month=6, day=5)
print(birthday)


import random

quotes = open("quotes.txt", 'r')
data = [line.split(',') for line in quotes.readlines()]
quotes.close()
print(data[random.randint(0,len(data))])
