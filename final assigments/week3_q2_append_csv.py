'''
Program to append user details to "records.csv"
Takes input for: student_name, roll_no, program, year, group
'''

import csv
import os

# Function to append records to CSV
def append_records():
    filename = "records.csv"
    
    # Check if file exists, if not create with headers
    file_exists = os.path.exists(filename)
    
    if not file_exists:
        # Create file with headers
        try:
            with open(filename, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['student_name', 'roll_no', 'program', 'year', 'group'])
                writer.writeheader()
            print(f"\n✓ File '{filename}' created successfully with headers")
        except Exception as e:
            print(f"\nError creating file: {e}")
            return
    
    # Append new records
    try:
        print("\n" + "="*50)
        print("ADD NEW STUDENT RECORD")
        print("="*50)
        
        while True:
            # Get student details
            student_name = input("\nEnter student name: ").strip()
            roll_no = input("Enter roll number: ").strip()
            program = input("Enter program (B.Tech/BCA/etc): ").strip()
            year = input("Enter year (1/2/3/4): ").strip()
            group = input("Enter group (A/B/C/etc): ").strip()
            
            # Validate inputs
            if not all([student_name, roll_no, program, year, group]):
                print("Error: All fields are required!")
                continue
            
            # Append to CSV
            with open(filename, 'a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['student_name', 'roll_no', 'program', 'year', 'group'])
                writer.writerow({
                    'student_name': student_name,
                    'roll_no': roll_no,
                    'program': program,
                    'year': year,
                    'group': group
                })
            
            print("✓ Record added successfully!")
            
            # Ask if user wants to add more
            add_more = input("\nAdd another record? (yes/no): ").lower()
            if add_more != 'yes' and add_more != 'y':
                print("\nThank you!")
                break
    
    except Exception as e:
        print(f"\nError: {e}")

# Main program
if __name__ == "__main__":
    append_records()
