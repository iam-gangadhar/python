marks = input("Enter Student Marks with Space. ").split()

High = 0
for m in marks:
    k = int(m)
    if k >= High:
        High = k

print('Highest Score Marks is : ', High)