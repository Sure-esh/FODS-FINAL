'''
Program to find all prime numbers in a user-defined range
Displays: all primes, count of primes, and sum of primes
'''

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Take range input from user
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

# Find all primes in range
primes = []
for number in range(start, end + 1):
    if is_prime(number):
        primes.append(number)

# Calculate count and sum
count = len(primes)
total = sum(primes)

# Display results
print("\n" + "="*50)
print(f"PRIME NUMBERS BETWEEN {start} AND {end}")
print("="*50)
print(f"Prime Numbers: {primes}")
print("-"*50)
print(f"Count of Primes: {count}")
print(f"Sum of Primes:   {total}")
print("="*50)
