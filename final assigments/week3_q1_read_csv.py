'''
Program to read a CSV file "records.csv" and display its contents
Fields: student_name, roll_no, program, year, group
'''

# Import csv module
import csv
import os

# Function to read and display CSV file
def read_records():
    filename = "records.csv"
    
    # Check if file exists
    if not os.path.exists(filename):
        print(f"\nError: File '{filename}' does not exist!")
        print("Please create the file first with student records.")
        return
    
    try:
        # Open and read CSV file
        print("\n" + "="*70)
        print("STUDENT RECORDS")
        print("="*70 + "\n")
        
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            
            # Check if file has data
            if reader.fieldnames is None:
                print("File is empty!")
                return
            
            # Display header
            print(f"{'Student Name':<20} {'Roll No':<12} {'Program':<15} {'Year':<6} {'Group':<8}")
            print("-" * 70)
            
            # Display each record
            record_count = 0
            for row in reader:
                if row:
                    print(f"{row.get('student_name', ''):<20} {row.get('roll_no', ''):<12} {row.get('program', ''):<15} {row.get('year', ''):<6} {row.get('group', ''):<8}")
                    record_count += 1
            
            print("-" * 70)
            print(f"Total Records: {record_count}")
            print("="*70)
    
    except Exception as e:
        print(f"\nError reading file: {e}")

# Main program
if __name__ == "__main__":
    read_records()
