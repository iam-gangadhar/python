# Here we are tryting to add values to Dictonary.

student_list = [
    {"name": "gangadhar",
     "marks": 780,
     "rank": "First Class"}]

def AddStudent(name, marks, rank):
    new_student = {}
    new_student["name"] = name
    new_student["marks"] = marks
    new_student["rank"] = rank
    student_list.append(new_student)

print("before Adding Student : ",student_list)
AddStudent("Ramu",780, "SecondClass")
AddStudent("Kumari",880, "Distent Pass")
AddStudent("Keerthi", 980, "State First")
print("After Adding student List", student_list)

