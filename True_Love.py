name1 = input('Enter your Name ').lower()
name2 = input('Enter Your Partner Name').lower()
fname = name1+name2
true =['t','r','u','e']
love =['l','o','v','e']
T,L = 0,0
for i in true:
    total = fname.count(i)
    T += total
for k in love:
    total = fname.count(k)
    L += total

total = int(str(T)+str(L))
if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total > 40 and total < 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")

