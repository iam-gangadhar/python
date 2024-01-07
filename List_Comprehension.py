# Using List Comprehension to create new list

numbers = [1, 2, 3, 4, 5]
new_numbers = [n + 1 for n in numbers]
print("Before Adding Numbers", numbers)
print("After Adding Numbers", new_numbers)

# using String in List comprehension
name = "Gangadhar"
my_name = [l for l in name]
print(my_name)

# Using Range in list comprehension
my_range = [i + i for i in range(1, 5)]
print(my_range)

# Conditional List Comprehension
names = ['Gangadhar', 'Kumari', "Surya", "Siddhu", "Keerthi", "ram", "Kum"]
short_names = [name for name in names if len(name) <= 5]
print(short_names)

# Dictionary Comprehension
import random

student_scores = {n: random.randint(30, 99) for n in names}
print(student_scores)
passed_students = {student: score for (student, score) in student_scores.items() if score >= 50}
print(passed_students)

# message = input("Enter Your Message : ")
# message = message.split()
# message_count = {word:len(word) for word in message}
# print(message_count)
# weather_c = eval(input())
# print(weather_c)

# using data frame
# import pandas as p
#
# student_dict = {'Gangadhar': 96, 'Kumari': 84, 'Surya': 99, 'Siddhu': 52, 'Keerthi': 67, 'ram': 30, 'Kum': 91}
# student_data = p.DataFrame(student_dict)
# print(student_data)
