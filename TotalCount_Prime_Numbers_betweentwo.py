def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes_between(start, end):
    count = 0
    for num in range(start, end + 1):
        if is_prime(num):
            count += 1
    return count

# Input
start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))

# Count primes and display the result
result = count_primes_between(start_num, end_num)
print(f'The number of prime numbers between {start_num} and {end_num} is: {result}')