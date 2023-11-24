from array import *
# here i means integer in array and you can use 'u' for single character
arr = array('i', [])

for i in range(5):
    x = input("Enter The Elements, : ")
    arr.append(int(x))

reverse_arr = arr[::-1]
print(reverse_arr)
