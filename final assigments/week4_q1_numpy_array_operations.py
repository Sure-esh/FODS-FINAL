'''
NumPy Program 1: Array Operations
Perform: sum, mean, max, min values on array
'''

import numpy as np

# Program for array operations
print("="*60)
print("NumPy Array Operations")
print("="*60)

# Create array
array = np.array([10, 20, 30, 40, 50])

print("\nArray: ", array)

# Perform operations
total_sum = np.sum(array)
mean_value = np.mean(array)
max_value = np.max(array)
min_value = np.min(array)

# Display results
print("\n" + "-"*60)
print("Array Operations:")
print("-"*60)
print(f"a) Total Sum:        {total_sum}")
print(f"b) Mean Value:       {mean_value}")
print(f"c) Largest Value:    {max_value}")
print(f"   Smallest Value:   {min_value}")
print("="*60)
