'''
NumPy Program 3: Random Array, Sorting, and Reshaping
Create array of random integers
Sort and reshape into matrix
'''

import numpy as np

# Program for random array and reshaping
print("="*60)
print("Random Array, Sorting, and Reshaping")
print("="*60)

# Generate array of 12 random integers
array = np.random.randint(1, 100, size=12)

print("\nOriginal Random Array (1x12):")
print(array)

# Sort the array
sorted_array = np.sort(array)
print("\nSorted Array:")
print(sorted_array)

# Reshape to 3x4
print("\n" + "-"*60)
print("Reshaped to 3x4 Matrix:")
print("-"*60)
matrix_3x4 = sorted_array.reshape(3, 4)
print(matrix_3x4)

# Reshape to 4x3
print("\nReshaped to 4x3 Matrix:")
print("-"*60)
matrix_4x3 = sorted_array.reshape(4, 3)
print(matrix_4x3)

print("\n" + "="*60)
print(f"Original Size: {array.size} elements")
print(f"Matrix 1: {matrix_3x4.shape[0]}x{matrix_3x4.shape[1]}")
print(f"Matrix 2: {matrix_4x3.shape[0]}x{matrix_4x3.shape[1]}")
print("="*60)
