'''
Program to find numbers divisible by 9 but not by 6 in a user-defined range
Default range: 1000 to 2500
User can enter custom range
'''

# Ask user if they want custom range or default
choice = input("Use default range (1000-2500)? (yes/no): ").lower()

if choice == 'no' or choice == 'n':
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))
else:
    start = 1000
    end = 2500

# Find numbers divisible by 9 but not by 6
numbers = []
for num in range(start, end + 1):
    if num % 9 == 0 and num % 6 != 0:
        numbers.append(num)

# Display results
print("\n" + "="*50)
print(f"NUMBERS DIVISIBLE BY 9 BUT NOT BY 6")
print(f"RANGE: {start} to {end}")
print("="*50)
print(f"Numbers: {numbers}")
print("-"*50)
print(f"Total Count: {len(numbers)}")
print("="*50)
