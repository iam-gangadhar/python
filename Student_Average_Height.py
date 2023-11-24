# Taking Input from user students height as List using split function
student_height = input("Enter Students height with space ").split()

#converting string inputs to integer using for loop
for n in range(0,len(student_height)):
    student_height[n] = int(student_height[n])

#counting total students using len function
total_students = len(student_height)
average_height = round(sum(student_height)/total_students)
print(total_students)
print(average_height)
