'''
Pandas & Matplotlib Program 1: Read CSV and Create Plots
Read "health_data.csv"
Create scatter plots for relationships:
- weight vs height
- age vs weight
- height vs age
- gender vs height
- gender vs weight
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Program to read CSV and create plots
print("="*60)
print("Health Data Analysis with Plots")
print("="*60)

# Create sample health data if file doesn't exist
import os

if not os.path.exists("health_data.csv"):
    # Create sample data
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

print("\nData loaded successfully!")
print(f"Rows: {len(df)}")
print("\nFirst few records:")
print(df.head())

# Create plots
print("\nGenerating plots...")

# Create figure with subplots
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Health Data Analysis', fontsize=16, fontweight='bold')

# Plot 1: Weight vs Height
axes[0, 0].scatter(df['height'], df['weight'], color='blue', s=50)
axes[0, 0].set_xlabel('Height')
axes[0, 0].set_ylabel('Weight')
axes[0, 0].set_title('Weight vs Height')
axes[0, 0].grid(True, alpha=0.3)

# Plot 2: Age vs Weight
axes[0, 1].scatter(df['age'], df['weight'], color='green', s=50)
axes[0, 1].set_xlabel('Age')
axes[0, 1].set_ylabel('Weight')
axes[0, 1].set_title('Age vs Weight')
axes[0, 1].grid(True, alpha=0.3)

# Plot 3: Height vs Age
axes[0, 2].scatter(df['age'], df['height'], color='red', s=50)
axes[0, 2].set_xlabel('Age')
axes[0, 2].set_ylabel('Height')
axes[0, 2].set_title('Height vs Age')
axes[0, 2].grid(True, alpha=0.3)

# Plot 4: Gender vs Height
gender_height = df.groupby('gender')['height'].apply(list)
axes[1, 0].scatter(['M']*len(gender_height.get('M', [])), gender_height.get('M', []), label='Male', color='blue', s=50)
axes[1, 0].scatter(['F']*len(gender_height.get('F', [])), gender_height.get('F', []), label='Female', color='red', s=50)
axes[1, 0].set_ylabel('Height')
axes[1, 0].set_title('Gender vs Height')
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3)

# Plot 5: Gender vs Weight
gender_weight = df.groupby('gender')['weight'].apply(list)
axes[1, 1].scatter(['M']*len(gender_weight.get('M', [])), gender_weight.get('M', []), label='Male', color='blue', s=50)
axes[1, 1].scatter(['F']*len(gender_weight.get('F', [])), gender_weight.get('F', []), label='Female', color='red', s=50)
axes[1, 1].set_ylabel('Weight')
axes[1, 1].set_title('Gender vs Weight')
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3)

# Hide the last subplot
axes[1, 2].axis('off')

plt.tight_layout()
plt.savefig('health_plots.png', dpi=100, bbox_inches='tight')
print("\n✓ Plots saved as 'health_plots.png'")

plt.show()
print("\n" + "="*60)
