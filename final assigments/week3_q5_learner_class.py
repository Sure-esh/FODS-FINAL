'''
Program to create a Learner class with attributes
Class includes: roll_no, full_name, address, enrollment_year, program, group
Instantiate object and display details
'''

# Define Learner class
class Learner:
    def __init__(self):
        # Initialize attributes
        self.roll_no = ""
        self.full_name = ""
        self.address = ""
        self.enrollment_year = ""
        self.program = ""
        self.group = ""
    
    # Method to take input
    def take_input(self):
        print("\n" + "="*50)
        print("LEARNER DETAILS INPUT")
        print("="*50 + "\n")
        
        self.roll_no = input("Enter roll number: ").strip()
        self.full_name = input("Enter full name: ").strip()
        self.address = input("Enter address: ").strip()
        self.enrollment_year = input("Enter enrollment year: ").strip()
        self.program = input("Enter program (B.Tech/BCA/etc): ").strip()
        self.group = input("Enter group (A/B/C/etc): ").strip()
    
    # Method to display details
    def display_details(self):
        print("\n" + "="*50)
        print("LEARNER DETAILS")
        print("="*50)
        print(f"Roll Number:      {self.roll_no}")
        print(f"Full Name:        {self.full_name}")
        print(f"Address:          {self.address}")
        print(f"Enrollment Year:  {self.enrollment_year}")
        print(f"Program:          {self.program}")
        print(f"Group:            {self.group}")
        print("="*50)

# Main program
if __name__ == "__main__":
    # Create learner object
    learner = Learner()
    
    # Take input
    learner.take_input()
    
    # Display details
    learner.display_details()
