
def Countbit(n):
    binary = str(bin(n))
    b = binary.split('b')
    ans = 0
    for i in b[1]:
        ans += int(i)
    print(ans)    


Countbit(5)
