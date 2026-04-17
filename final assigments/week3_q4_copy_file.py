'''
Program to copy content from one file to another
Takes input file and output file names from user
Uses try/except for error handling
'''

import os

# Function to copy file
def copy_file():
    print("\n" + "="*50)
    print("FILE COPY PROGRAM")
    print("="*50)
    
    try:
        # Get input file name
        input_file = input("\nEnter input file name: ").strip()
        
        # Check if input file exists
        if not os.path.exists(input_file):
            print(f"Error: Input file '{input_file}' does not exist!")
            return
        
        # Get output file name
        output_file = input("Enter output file name: ").strip()
        
        # Check if output file already exists
        if os.path.exists(output_file):
            print(f"Error: Output file '{output_file}' already exists!")
            overwrite = input("Do you want to overwrite? (yes/no): ").lower()
            if overwrite != 'yes' and overwrite != 'y':
                print("Copy operation cancelled.")
                return
        
        # Copy file
        try:
            with open(input_file, 'r') as infile:
                content = infile.read()
            
            with open(output_file, 'w') as outfile:
                outfile.write(content)
            
            print(f"\n✓ File copied successfully!")
            print(f"Input file:  {input_file}")
            print(f"Output file: {output_file}")
            
            # Display file statistics
            file_size = os.path.getsize(output_file)
            line_count = len(content.split('\n'))
            print(f"\nFile Statistics:")
            print(f"  Size: {file_size} bytes")
            print(f"  Lines: {line_count}")
        
        except IOError as e:
            print(f"Error reading/writing file: {e}")
    
    except Exception as e:
        print(f"Error: {e}")

# Main program
if __name__ == "__main__":
    copy_file()
