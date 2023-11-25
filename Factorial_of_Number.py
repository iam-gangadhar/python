
def Factorial(num):
    fact = 1
    for n in range(1,num+1):
        fact *= n
    return fact

print(Factorial(10))