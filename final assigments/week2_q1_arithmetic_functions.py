'''
Function-based program for arithmetic operations
Takes two integers and displays sum, difference, product, quotient
'''

# Function to perform arithmetic operations
def arithmetic_operations(num1, num2):
    addition = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    quotient = num1 / num2
    
    return addition, difference, product, quotient

# Main program
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Call function
sum_val, diff_val, prod_val, quot_val = arithmetic_operations(num1, num2)

# Display results
print("\n" + "="*50)
print("ARITHMETIC OPERATIONS RESULTS")
print("="*50)
print(f"Sum:         {num1} + {num2} = {sum_val}")
print(f"Difference:  {num1} - {num2} = {diff_val}")
print(f"Product:     {num1} × {num2} = {prod_val}")
print(f"Quotient:    {num1} ÷ {num2} = {quot_val:.2f}")
print("="*50)
