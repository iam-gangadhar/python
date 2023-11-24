
# Adding Values to Array First we will import Array
from array import *

marks = array('i', [])

#collecting values from for loop
for i in range(4):
    n = int(input("Enter Valu's to Add an Array :"))
    marks.append(n)
print(marks)
# Removing Value from Array 
r = int(input('Enter Value that you want to remove :'))
for i in marks:
    if r == i:
        marks.remove(i)

print(marks)