'''
Function to count occurrences of each number in a list
Returns a dictionary showing frequency of each number
Tests with multiple lists
'''

# Function to count occurrences
def count_occurrences(numbers):
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    return frequency

# Test with 3 different lists
print("="*50)
print("COUNT OCCURRENCES IN LISTS")
print("="*50)

# List 1
list1 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
result1 = count_occurrences(list1)
print(f"\nList 1: {list1}")
print(f"Frequency: {result1}")

# List 2
list2 = [5, 5, 10, 10, 10, 15, 20, 20]
result2 = count_occurrences(list2)
print(f"\nList 2: {list2}")
print(f"Frequency: {result2}")

# List 3
list3 = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
result3 = count_occurrences(list3)
print(f"\nList 3: {list3}")
print(f"Frequency: {result3}")

print("\n" + "="*50)
