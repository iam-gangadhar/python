student_heights = input().split()

total = 0
sum = len(student_heights)
for i in student_heights:
    total += int(i)

avg = round(total/sum)
avg = round(total/sum)
print(f'total height = {total}')
print(f'number of students = {sum}')
print(f'average height = {avg}')

