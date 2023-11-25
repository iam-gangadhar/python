# A Function Calling Itself called Recurssion 993 times calling 
i = 0
def recurrsion():
    global i
    print('Helo python',i)
    i += 1
    recurrsion()

recurrsion()