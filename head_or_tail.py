import random

choice = random.randint(0,1)
if choice == 1:
    print("Heads")
else:
    print('Tails')

# List Data stracuture in Python Example.
num = [1,123,413,"sdfas"]
num[0] = 'updated'
num.append('Iaminsidelist')
print(num[1])
print(num)
print(num[-1])
num.extend([12,423,12,2])
print(num)
