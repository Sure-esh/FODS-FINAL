'''
Program to calculate cube, cube root, logarithms, and power of 6
Uses math library for calculations
'''

import math

# Take input from user
number = float(input("Enter a number: "))

# Calculate all values
cube = number ** 3
cube_root = number ** (1/3)
natural_log = math.log(number)  # Natural logarithm (ln)
log_base2 = math.log2(number)   # Base-2 logarithm
power_6 = number ** 6

# Display results in clean format
print("\n" + "="*50)
print("MATHEMATICAL OPERATIONS RESULTS")
print("="*50)
print(f"Number: {number}")
print("-"*50)
print(f"I.   Cube:              {number}³ = {cube}")
print(f"II.  Cube Root:         ∛{number} = {cube_root:.4f}")
print(f"III. Natural Log:       ln({number}) = {natural_log:.4f}")
print(f"IV.  Base-2 Log:        log₂({number}) = {log_base2:.4f}")
print(f"V.   Power of 6:        {number}⁶ = {power_6}")
print("="*50)
