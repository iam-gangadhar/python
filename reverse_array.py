from array import *
# here i means integer in array and you can use 'u' for single character
arr = array('i',[5])

for i in range(4):
    n = int(input('Enter the Values'))
    arr.append(n)
print(arr)
print("after reversing the Array")


res = arr[: : -1]    #1st method to reverse the array
print(arr.reverse()) #2nd Method using reverse method

print(arr)
print(res)
