
def is_leap(year):
  if (year % 400 == 0) and (year % 100 == 0):
    return True
  elif (year % 4 == 0) and (year % 100 != 0):
    return True
  else:
    return False
  
# TODO: Add more code here 👇
    
def days_in_month(year,month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if is_leap(year=year):
    month_days[1] = 29
  return month_days[month-1]


#🚨 Do NOT change any of the code below
   
year = int(input()) # Enter a year
month = int(input()) # Enter a month

days = days_in_month(year, month)
print(days)