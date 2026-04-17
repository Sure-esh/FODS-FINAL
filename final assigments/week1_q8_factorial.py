'''
Program to calculate factorial of a number
Includes input validation to ensure positive integer
'''

# Function to calculate factorial
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial

# Take input from user
try:
    number = int(input("Enter a positive integer: "))
    
    # Validate input
    if number < 0:
        print("Invalid input! Please enter a positive integer.")
    else:
        # Calculate and display factorial
        result = calculate_factorial(number)
        print("\n" + "="*50)
        print(f"Factorial of {number}")
        print("="*50)
        print(f"{number}! = {result}")
        print("="*50)

except ValueError:
    print("Invalid input! Please enter a positive integer.")
