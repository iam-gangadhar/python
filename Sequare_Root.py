#Two Ways We can find Sequare Root 1st way using math.square function
import math
n = int(input("Enter Number to Find Sequare Root: "))
ans = math.sqrt(n)
print("Answer is : ",ans)

# Second Way we using Exponentiation operator

ans2 = n ** 0.5
print("Second Way Answer is ", ans2)
