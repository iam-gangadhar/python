
# Checking Each Number Prime or Not
def is_prime(num):
    if num < 2:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i==0:
                return False
        return True

prime_numbers = []
def CountSumofPrimenumbers(start, end):
    sum_of_prime = 0
    for k in range(start, end+1):
        if is_prime(k):
            sum_of_prime += k
            prime_numbers.append(k)

    print(f"Sum of Total Prime Numbers between {start} and {end} is : {sum_of_prime}")
    print("Total Prime Numbers are : \n",prime_numbers)


start_num = int(input("Enter Starting Number: "))
end_num = int(input("Enter the Ending Number: "))

CountSumofPrimenumbers(start=start_num, end=end_num)


