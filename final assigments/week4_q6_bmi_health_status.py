'''
Pandas Program 2: Read CSV, Add New Columns, Calculate BMI and Health Status
Read "health_data.csv"
Add columns: BMI and Health_Status
Calculate based on provided conditions
'''

import pandas as pd
import os

# Program to read CSV and add BMI and Health Status
print("="*70)
print("Health Data Analysis with BMI and Health Status")
print("="*70)

# Create sample health data if file doesn't exist
if not os.path.exists("health_data.csv"):
    data = {
        'age': [25, 30, 35, 28, 32, 40, 22, 38, 27, 45, 33, 29, 36, 24, 42],
        'height': [165, 170, 175, 168, 172, 178, 160, 176, 166, 180, 171, 169, 174, 162, 179],
        'weight': [65, 72, 78, 70, 75, 82, 60, 80, 68, 85, 73, 71, 76, 58, 83],
        'gender': ['M', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'F', 'M']
    }
    df = pd.DataFrame(data)
    df.to_csv("health_data.csv", index=False)
    print("\n✓ Sample health_data.csv created")
else:
    df = pd.read_csv("health_data.csv")

print("\nOriginal Data:")
print(df.head(10))

# Function to calculate BMI
def calculate_bmi(weight, height):
    # BMI = Weight / Height
    return weight / height

# Function to determine health status based on BMI
def get_health_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Healthy range"
    elif 25 <= bmi <= 29.9:
        return "Overweight risk"
    elif 30 <= bmi <= 34.9:
        return "High risk of diabetes/heart disease"
    else:  # BMI >= 40
        return "Critical health condition"

# Calculate BMI
df['BMI'] = df.apply(lambda row: calculate_bmi(row['weight'], row['height']), axis=1)

# Calculate Health Status
df['Health_Status'] = df['BMI'].apply(get_health_status)

# Display results
print("\n" + "="*70)
print("Data with BMI and Health Status")
print("="*70)
print(df.to_string(index=False))

# Statistics
print("\n" + "-"*70)
print("Health Status Distribution:")
print("-"*70)
status_count = df['Health_Status'].value_counts()
for status, count in status_count.items():
    percentage = (count / len(df)) * 100
    print(f"{status:<45} : {count:>3} persons ({percentage:>5.1f}%)")

# BMI Statistics
print("\n" + "-"*70)
print("BMI Statistics:")
print("-"*70)
print(f"Average BMI:     {df['BMI'].mean():.2f}")
print(f"Minimum BMI:     {df['BMI'].min():.2f}")
print(f"Maximum BMI:     {df['BMI'].max():.2f}")
print(f"Standard Dev:    {df['BMI'].std():.2f}")

# Save updated data
df.to_csv("health_data_updated.csv", index=False)
print("\n✓ Updated data saved to 'health_data_updated.csv'")

print("\n" + "="*70)
