def fibonacciNumber(n):
    # Write your code here.
    mod = 10**9+7
    a , b = 0, 1
    for i in range(2, n+1):
        a, b = b, (a+b)% mod
    return b

Fibo = fibonacciNumber(int(input("Enter the Number")))
print(Fibo)

