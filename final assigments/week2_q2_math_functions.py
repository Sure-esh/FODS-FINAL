'''
Separate functions for mathematical operations
Each function takes two inputs and returns the result
'''

# Function 1: Addition
def add(a, b):
    return a + b

# Function 2: Multiplication
def multiply(a, b):
    return a * b

# Function 3: Division
def divide(a, b):
    return a / b

# Function 4: Floor Division
def floor_divide(a, b):
    return a // b

# Function 5: Exponentiation
def power(a, b):
    return a ** b

# Main program
print("="*50)
print("MATHEMATICAL OPERATIONS USING FUNCTIONS")
print("="*50)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Call all functions
addition_result = add(num1, num2)
multiplication_result = multiply(num1, num2)
division_result = divide(num1, num2)
floor_division_result = floor_divide(num1, num2)
power_result = power(num1, num2)

# Display results
print("\n" + "="*50)
print("RESULTS")
print("="*50)
print(f"I.   Addition:       {num1} + {num2} = {addition_result}")
print(f"II.  Multiplication: {num1} × {num2} = {multiplication_result}")
print(f"III. Division:       {num1} ÷ {num2} = {division_result:.2f}")
print(f"IV.  Floor Division: {num1} // {num2} = {floor_division_result}")
print(f"V.   Exponentiation: {num1} ^ {num2} = {power_result}")
print("="*50)
