import logo

print(logo.Logo)

def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations = {
    "+" : add,
    "-" : sub,
    "*" : multiply,
    "/" : divide
}
calc = True
num1 =float(input("What's the first number?: "))
for item in operations:
    print(item)
    
while calc:
    symbol = input("Pick an operation fron the line above: ")
    num2 = float(input("What's the next number?: "))
    t = operations[symbol]
    first_answer = t(n1=num1,n2=num2)
    print(f"{num1} {symbol} {num2} = {first_answer}")
    
    user = input(f"Tyep 'y' to continuee calculating with {first_answer}, or type 'n' to exti: ")
    if user == 'y':
        calc = True
        num1 = first_answer
    else:
        calc = False
