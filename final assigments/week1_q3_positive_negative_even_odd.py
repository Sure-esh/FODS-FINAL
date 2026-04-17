'''
Program to check if a number is positive/negative and even/odd
Classifies number into one of five categories
'''

# Take input from user
number = int(input("Enter a number: "))

# Check if positive or negative
if number > 0:
    sign = "Positive"
elif number < 0:
    sign = "Negative"
else:
    sign = "Zero"

# Check if even or odd
if number == 0:
    category = "Zero"
elif number > 0:
    if number % 2 == 0:
        category = "Positive Even"
    else:
        category = "Positive Odd"
else:  # number < 0
    if number % 2 == 0:
        category = "Negative Even"
    else:
        category = "Negative Odd"

# Display result
print("\n" + "="*50)
print(f"Number Entered: {number}")
print("-"*50)
print(f"Classification: {category}")
print("="*50)
