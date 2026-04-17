'''
Program to create Staff class and manage staff data
Class attributes: emp_id, full_name, address, phone_number, marital_status, dependents, salary
Save to "staff.csv", view and search staff details
Uses try/except for error handling
'''

import csv
import os

# Define Staff class
class Staff:
    def __init__(self, emp_id, full_name, address, phone_number, marital_status, dependents, salary):
        self.emp_id = emp_id
        self.full_name = full_name
        self.address = address
        self.phone_number = phone_number
        self.marital_status = marital_status
        self.dependents = dependents
        self.salary = salary
    
    # Method to display staff details
    def display(self):
        print(f"ID: {self.emp_id} | Name: {self.full_name} | Salary: {self.salary}")

# Define StaffManagement class
class StaffManagement:
    def __init__(self, filename="staff.csv"):
        self.filename = filename
        self.staff_list = []
    
    # Method to create CSV file with headers if not exists
    def create_file(self):
        try:
            if not os.path.exists(self.filename):
                with open(self.filename, 'w', newline='') as file:
                    fieldnames = ['emp_id', 'full_name', 'address', 'phone_number', 'marital_status', 'dependents', 'salary']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                print(f"✓ File '{self.filename}' created successfully")
        except Exception as e:
            print(f"Error creating file: {e}")
    
    # Method to add staff
    def add_staff(self, staff):
        try:
            with open(self.filename, 'a', newline='') as file:
                fieldnames = ['emp_id', 'full_name', 'address', 'phone_number', 'marital_status', 'dependents', 'salary']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writerow({
                    'emp_id': staff.emp_id,
                    'full_name': staff.full_name,
                    'address': staff.address,
                    'phone_number': staff.phone_number,
                    'marital_status': staff.marital_status,
                    'dependents': staff.dependents,
                    'salary': staff.salary
                })
            print(f"✓ Staff member '{staff.full_name}' added successfully")
        except Exception as e:
            print(f"Error adding staff: {e}")
    
    # Method to view all staff
    def view_all_staff(self):
        try:
            if not os.path.exists(self.filename):
                print("No staff records found!")
                return
            
            print("\n" + "="*100)
            print("STAFF LIST")
            print("="*100)
            
            with open(self.filename, 'r') as file:
                reader = csv.DictReader(file)
                print(f"{'ID':<6} {'Name':<20} {'Phone':<12} {'Status':<10} {'Dependents':<10} {'Salary':<12}")
                print("-"*100)
                
                count = 0
                for row in reader:
                    if row['emp_id']:  # Skip header
                        print(f"{row['emp_id']:<6} {row['full_name']:<20} {row['phone_number']:<12} {row['marital_status']:<10} {row['dependents']:<10} {row['salary']:<12}")
                        count += 1
                
                print("-"*100)
                print(f"Total Staff: {count}")
                print("="*100)
        except Exception as e:
            print(f"Error viewing staff: {e}")
    
    # Method to search staff by ID
    def search_staff(self, emp_id):
        try:
            if not os.path.exists(self.filename):
                print("No staff records found!")
                return None
            
            with open(self.filename, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['emp_id'] == emp_id:
                        return row
            
            print(f"Staff with ID {emp_id} not found!")
            return None
        except Exception as e:
            print(f"Error searching staff: {e}")
            return None

# Main program
if __name__ == "__main__":
    # Create management system
    mgmt = StaffManagement()
    mgmt.create_file()
    
    print("\n" + "="*50)
    print("STAFF MANAGEMENT SYSTEM")
    print("="*50)
    
    while True:
        print("\nOptions:")
        print("1. Add staff member")
        print("2. View all staff")
        print("3. Search staff by ID")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1/2/3/4): ").strip()
        
        if choice == '1':
            try:
                emp_id = input("Enter employee ID: ").strip()
                full_name = input("Enter full name: ").strip()
                address = input("Enter address: ").strip()
                phone = input("Enter phone number: ").strip()
                marital = input("Enter marital status (Single/Married): ").strip()
                dependents = input("Enter number of dependents: ").strip()
                salary = input("Enter salary: ").strip()
                
                staff = Staff(emp_id, full_name, address, phone, marital, dependents, salary)
                mgmt.add_staff(staff)
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == '2':
            mgmt.view_all_staff()
        
        elif choice == '3':
            search_id = input("Enter employee ID to search: ").strip()
            result = mgmt.search_staff(search_id)
            if result:
                print("\n" + "-"*50)
                print(f"ID: {result['emp_id']}")
                print(f"Name: {result['full_name']}")
                print(f"Address: {result['address']}")
                print(f"Phone: {result['phone_number']}")
                print(f"Marital Status: {result['marital_status']}")
                print(f"Dependents: {result['dependents']}")
                print(f"Salary: {result['salary']}")
                print("-"*50)
        
        elif choice == '4':
            print("Exiting... Thank you!")
            break
        
        else:
            print("Invalid choice! Please try again.")
