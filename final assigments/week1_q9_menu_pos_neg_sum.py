'''
Menu-driven program to calculate separate sums of positive and negative numbers
User can add numbers or exit anytime
'''

# Initialize variables
positive_sum = 0
negative_sum = 0
positive_count = 0
negative_count = 0

print("="*50)
print("POSITIVE AND NEGATIVE SUM CALCULATOR")
print("="*50)

# Loop for menu
while True:
    print("\nOptions:")
    print("1. Add a number")
    print("2. View current sums")
    print("3. Exit program")
    
    choice = input("\nEnter your choice (1/2/3): ")
    
    if choice == '1':
        try:
            number = int(input("Enter a number: "))
            
            if number > 0:
                positive_sum += number
                positive_count += 1
                print(f"✓ Added {number} to positive sum")
            elif number < 0:
                negative_sum += number
                negative_count += 1
                print(f"✓ Added {number} to negative sum")
            else:
                print("Zero is neither positive nor negative")
        
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    elif choice == '2':
        print("\n" + "-"*50)
        print("CURRENT SUMS:")
        print("-"*50)
        print(f"Positive Numbers Count: {positive_count}")
        print(f"Positive Sum:           {positive_sum}")
        print(f"Negative Numbers Count: {negative_count}")
        print(f"Negative Sum:           {negative_sum}")
        print("-"*50)
    
    elif choice == '3':
        print("\n" + "="*50)
        print("FINAL RESULTS:")
        print("="*50)
        print(f"Positive Sum: {positive_sum}")
        print(f"Negative Sum: {negative_sum}")
        print("="*50)
        print("Program ended. Thank you!")
        break
    
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
