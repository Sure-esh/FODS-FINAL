'''
NumPy Program 2: List Sorting and Slicing
Take list input (at least 12 elements)
Sort and perform slicing operations on index ranges
'''

import numpy as np

# Program for sorting and slicing
print("="*60)
print("Sorting and Slicing Operations")
print("="*60)

# Get number of elements
num_elements = int(input("\nEnter number of elements (minimum 12): "))

if num_elements < 12:
    print("Error: Please enter at least 12 elements!")
else:
    # Get list from user
    numbers = []
    print(f"Enter {num_elements} numbers:")
    for i in range(num_elements):
        num = int(input(f"Number {i+1}: "))
        numbers.append(num)
    
    # Convert to NumPy array
    arr = np.array(numbers)
    
    # Sort the array
    sorted_arr = np.sort(arr)
    
    print("\n" + "-"*60)
    print("Original Array:", arr)
    print("Sorted Array:  ", sorted_arr)
    print("-"*60)
    
    # Perform slicing operations
    print("\nSlicing Operations:")
    print(f"Indices 3-6:     {sorted_arr[3:7]}")
    print(f"Indices 6-9:     {sorted_arr[6:10]}")
    print(f"Indices 4-10:    {sorted_arr[4:11]}")
    
    print("="*60)
