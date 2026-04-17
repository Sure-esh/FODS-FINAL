'''
Function to check if a string is Armstrong number
An Armstrong number is equal to sum of its digits raised to power of number of digits
Example: 153 = 1^3 + 5^3 + 3^3
'''

# Function to check Armstrong number
def is_armstrong(num_str):
    # Remove spaces and convert to digits
    digits = [int(d) for d in num_str if d.isdigit()]
    
    # Calculate sum of digits raised to power of count
    num_digits = len(digits)
    armstrong_sum = sum(digit ** num_digits for digit in digits)
    original_number = int(''.join(map(str, digits)))
    
    return armstrong_sum == original_number

# Main program
input_string = input("Enter a string/number to check if it's Armstrong: ")

result = is_armstrong(input_string)

print("\n" + "="*50)
if result:
    print(f"✓ '{input_string}' IS an Armstrong number")
else:
    print(f"✗ '{input_string}' IS NOT an Armstrong number")
print("="*50)

# Example
print("\nExample: 153 is Armstrong because 1³ + 5³ + 3³ = 153")
