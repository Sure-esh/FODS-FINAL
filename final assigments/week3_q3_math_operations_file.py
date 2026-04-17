'''
Program to perform arithmetic operations and save results to a file
Operations: Addition, Subtraction, Multiplication, Division
Results saved with current date and time
'''

import os
from datetime import datetime

# Function to perform operations
def perform_operations():
    filename = "results.txt"
    
    print("\n" + "="*50)
    print("ARITHMETIC OPERATIONS")
    print("="*50)
    
    try:
        # Open file for appending
        with open(filename, 'a') as file:
            # Write timestamp
            file.write("\n" + "="*50 + "\n")
            file.write(f"Date & Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("="*50 + "\n")
            
            # Continue until user exits
            while True:
                try:
                    # Get two numbers
                    num1 = float(input("\nEnter first number: "))
                    num2 = float(input("Enter second number: "))
                    
                    # Perform operations
                    addition = num1 + num2
                    subtraction = num1 - num2
                    multiplication = num1 * num2
                    
                    # Handle division by zero
                    if num2 != 0:
                        division = num1 / num2
                    else:
                        division = "Cannot divide by zero"
                    
                    # Display results
                    print("\n" + "-"*50)
                    print(f"Number 1: {num1}")
                    print(f"Number 2: {num2}")
                    print("-"*50)
                    print(f"Addition:        {num1} + {num2} = {addition}")
                    print(f"Subtraction:     {num1} - {num2} = {subtraction}")
                    print(f"Multiplication:  {num1} × {num2} = {multiplication}")
                    print(f"Division:        {num1} ÷ {num2} = {division}")
                    print("-"*50)
                    
                    # Write to file
                    file.write(f"\nOperation {datetime.now().strftime('%H:%M:%S')}:\n")
                    file.write(f"  Addition:        {num1} + {num2} = {addition}\n")
                    file.write(f"  Subtraction:     {num1} - {num2} = {subtraction}\n")
                    file.write(f"  Multiplication:  {num1} × {num2} = {multiplication}\n")
                    file.write(f"  Division:        {num1} ÷ {num2} = {division}\n")
                    
                    # Ask to continue
                    continue_choice = input("\nPerform another operation? (yes/no): ").lower()
                    if continue_choice != 'yes' and continue_choice != 'y':
                        break
                
                except ValueError:
                    print("Error: Please enter valid numbers!")
        
        # Display file contents
        print("\n" + "="*50)
        print("FILE CONTENTS")
        print("="*50 + "\n")
        
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
        
        print("\n✓ Results saved to '" + filename + "'")
    
    except Exception as e:
        print(f"\nError: {e}")

# Main program
if __name__ == "__main__":
    perform_operations()
