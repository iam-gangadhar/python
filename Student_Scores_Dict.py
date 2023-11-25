
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
student_grades = {}

for item in student_scores:
    if student_scores[item] >= 91:
        student_grades[item] = "Outstanding"
    elif student_scores[item]>=81 and student_scores[item]<=90:
        student_grades[item] = "Exceeds Expectations"
    elif student_scores[item]>=71 and student_scores[item]<=80:
        student_grades[item] = "Acceptable"
    else:
        student_grades[item] = "Fail"

for k, v in student_grades.items():
    print(k,'--',v)


