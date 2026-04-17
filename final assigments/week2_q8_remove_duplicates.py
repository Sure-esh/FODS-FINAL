'''
Program to remove duplicates from list and sort in ascending order
Takes user input and returns new list with duplicates removed and sorted
'''

# Function to remove duplicates and sort
def remove_duplicates_sort(numbers):
    # Remove duplicates by converting to set, then back to list
    unique_numbers = list(set(numbers))
    # Sort in ascending order
    unique_numbers.sort()
    return unique_numbers

# Main program
print("="*50)
print("REMOVE DUPLICATES AND SORT")
print("="*50)

# Get list from user
num_count = int(input("How many numbers do you want to enter? "))
numbers = []

print("Enter the numbers:")
for i in range(num_count):
    num = int(input(f"Number {i+1}: "))
    numbers.append(num)

# Process the list
result = remove_duplicates_sort(numbers)

# Display results
print("\n" + "="*50)
print("RESULTS")
print("="*50)
print(f"Original list:      {numbers}")
print(f"Unique sorted list: {result}")
print(f"Duplicates removed: {num_count - len(result)}")
print("="*50)
