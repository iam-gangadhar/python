student_scores = input().split()
x = 0
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  if x < student_scores[n]:
    x = student_scores[n]

print(f'The highest score in the class is: {x}')
