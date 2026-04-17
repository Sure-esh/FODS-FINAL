'''
Program to calculate total, average, percentage and grade for 6 subjects
Grade: Distinction (85%), First (70%), Second (55%), Third (45%), Fail (<45%)
'''

# Take marks for 6 subjects
print("Enter marks for 6 subjects (out of 100):\n")
marks = []
for i in range(1, 7):
    mark = float(input(f"Subject {i} marks: "))
    marks.append(mark)

# Calculate total and average
total = sum(marks)
average = total / 6
percentage = (total / 600) * 100

# Determine grade based on percentage
if percentage >= 85:
    grade = "Distinction"
elif percentage >= 70:
    grade = "First Division"
elif percentage >= 55:
    grade = "Second Division"
elif percentage >= 45:
    grade = "Third Division"
else:
    grade = "Fail"

# Display results
print("\n" + "="*50)
print("MARKS AND GRADE REPORT")
print("="*50)
print(f"Total Marks:        {total} / 600")
print(f"Average Marks:      {average:.2f}")
print(f"Percentage:         {percentage:.2f}%")
print("-"*50)
print(f"Grade:              {grade}")
print("="*50)
