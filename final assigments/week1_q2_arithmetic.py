'''
Program to take two integer inputs and display arithmetic operations
Operations: Addition, Multiplication, Division, Modulus, Exponentiation
'''

# Take input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate all operations
addition = num1 + num2
multiplication = num1 * num2
division = num1 / num2
modulus = num1 % num2
exponentiation = num1 ** num2

# Display results in clean format
print("\n" + "="*50)
print("ARITHMETIC OPERATIONS RESULTS")
print("="*50)
print(f"Number 1: {num1}")
print(f"Number 2: {num2}")
print("-"*50)
print(f"I.   Addition:          {num1} + {num2} = {addition}")
print(f"II.  Multiplication:    {num1} × {num2} = {multiplication}")
print(f"III. Division:          {num1} ÷ {num2} = {division:.2f}")
print(f"IV.  Modulus:           {num1} % {num2} = {modulus}")
print(f"V.   Exponentiation:    {num1} ^ {num2} = {exponentiation}")
print("="*50)
