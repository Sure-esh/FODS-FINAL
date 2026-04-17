'''
NumPy Program 4: Matrix Operations
Perform addition, subtraction, multiplication on matrices
Validate dimension compatibility
'''

import numpy as np

# Program for matrix operations
print("="*60)
print("Matrix Operations with Dimension Validation")
print("="*60)

try:
    # Get matrix dimensions
    rows1 = int(input("\nEnter rows for Matrix 1: "))
    cols1 = int(input("Enter columns for Matrix 1: "))
    
    rows2 = int(input("Enter rows for Matrix 2: "))
    cols2 = int(input("Enter columns for Matrix 2: "))
    
    # Validate dimensions
    if rows1 <= 0 or cols1 <= 0 or rows2 <= 0 or cols2 <= 0:
        raise ValueError("Dimensions must be positive!")
    
    # Create matrices
    print(f"\nEnter elements for Matrix 1 ({rows1}x{cols1}):")
    matrix1_list = []
    for i in range(rows1 * cols1):
        num = int(input(f"Element {i+1}: "))
        matrix1_list.append(num)
    
    matrix1 = np.array(matrix1_list).reshape(rows1, cols1)
    
    print(f"\nEnter elements for Matrix 2 ({rows2}x{cols2}):")
    matrix2_list = []
    for i in range(rows2 * cols2):
        num = int(input(f"Element {i+1}: "))
        matrix2_list.append(num)
    
    matrix2 = np.array(matrix2_list).reshape(rows2, cols2)
    
    print("\n" + "="*60)
    print("Matrix 1:")
    print(matrix1)
    print("\nMatrix 2:")
    print(matrix2)
    print("="*60)
    
    # Addition (requires same dimensions)
    if matrix1.shape == matrix2.shape:
        addition = matrix1 + matrix2
        print("\nAddition (A + B):")
        print(addition)
    else:
        print(f"\nError: Cannot add matrices with dimensions {matrix1.shape} and {matrix2.shape}")
    
    # Subtraction (requires same dimensions)
    if matrix1.shape == matrix2.shape:
        subtraction = matrix1 - matrix2
        print("\nSubtraction (A - B):")
        print(subtraction)
    else:
        print(f"\nError: Cannot subtract matrices with dimensions {matrix1.shape} and {matrix2.shape}")
    
    # Multiplication (requires cols1 == rows2)
    if cols1 == rows2:
        multiplication = np.dot(matrix1, matrix2)
        print(f"\nMultiplication (A × B):")
        print(multiplication)
    else:
        print(f"\nError: Cannot multiply matrices with dimensions {matrix1.shape} and {matrix2.shape}")
        print(f"For multiplication: columns of first matrix ({cols1}) must equal rows of second matrix ({rows2})")
    
    print("\n" + "="*60)

except ValueError as e:
    print(f"\nError: {e}")
except Exception as e:
    print(f"\nError: Invalid input!")
