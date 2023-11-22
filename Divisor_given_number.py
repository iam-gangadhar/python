from typing import List

#Getting All Divsors for Given Number 

def printDivisors(n: int) -> List[int]:
    # Write your code here
    divisors = []
    for i in range(1,n+1):
        if n%i == 0:
            divisors.append(i)
    return divisors

print(printDivisors(int(input('Enter Number '))))