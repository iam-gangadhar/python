import csv

# Reading data from CSV file and Taking values from that file created list
with open("weather_data.csv", mode='r') as data:
    n_data = csv.reader(data)
    temperatures = []
    for d in n_data:
        if d[1] != 'temp':
            temperatures.append(int(d[1]))
print(temperatures)

import pandas

mydata = pandas.read_csv("weather_data.csv")
print(type(mydata))
#t_mprature = mydata['temp']

#converting to the values in to list
t_mprature = mydata['temp'].to_list()
print(t_mprature)
average = sum(t_mprature)/len(t_mprature)
print(round(average))

# getting Largest Value in the list
maxvalue = mydata['temp'].max()
print(maxvalue)

#condtion checking
conditon = mydata["condition"].to_list()
print(conditon)

# getting Single Row
print(mydata[mydata.day == "Monday"])

# Getting row filter using highest Temperature row
print(mydata[mydata.temp == mydata['temp'].max()])

# Getting Specific Week  temperature and converting to forefather
monday =  mydata[mydata.day == "Monday"]
print(monday.condition)
#converting csv file to dictionary data type in pandas
# my_dict = mydata.to_dict()
# print(my_dict)
# data_html = mydata.to_html()
# print(data_html)



# Creating HTML File using write mode
# with open("myfile.html", mode='w') as web:
#     web.writelines(data_html)

# use documentation to work with pandas you can convert data to Excel, HTML , .


# Create a Dataframe from scratch
data_dict = {
    "students": ["Gangadhar", "Kumari", "Siddhu", "Keerthi", "Hello"],
    "scores": [787,455,7878,46,456]
}

s_data = pandas.DataFrame(data_dict)
s_data.to_csv("newdata.csv")
print(s_data)