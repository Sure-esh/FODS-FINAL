'''
Function to sort student names in reverse alphabetical order
Takes a list of names and returns sorted list in reverse order
'''

# Function to sort names in reverse alphabetical order
def sort_names_reverse(names):
    return sorted(names, reverse=True)

# Main program
print("="*50)
print("SORT STUDENT NAMES (REVERSE ALPHABETICAL)")
print("="*50)

try:
    # Get number of students
    num_students = int(input("\nEnter number of students: "))
    
    # Validate input
    if num_students <= 0:
        print("Error: Number of students must be greater than 0")
    else:
        # Get student names
        names = []
        print("\nEnter student names:")
        for i in range(num_students):
            name = input("Enter student {0} name: ".format(i+1))
            if name.strip():  # Only add non-empty names
                names.append(name.strip())
        
        if len(names) == 0:
            print("No names entered!")
        else:
            # Sort names in reverse alphabetical order
            sorted_names = sort_names_reverse(names)
            
            # Display results
            print("\n" + "-"*50)
            print("Original Order:")
            for name in names:
                print("  • " + name)
            
            print("\nReverse Alphabetical Order:")
            for name in sorted_names:
                print("  • " + name)
            print("-"*50)

except ValueError:
    print("Error: Please enter a valid number!")
