'''
Function key_value() to count character occurrences in a sentence
Returns a dictionary showing frequency of each character (excluding spaces)
'''

# Function to count character occurrences
def key_value(sentence):
    char_count = {}
    
    for char in sentence:
        # Ignore spaces
        if char != ' ':
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    return char_count

# Main program
print("="*50)
print("CHARACTER FREQUENCY IN SENTENCE")
print("="*50)

# Get sentence from user
sentence = input("Enter a sentence: ")

# Count characters
frequency = key_value(sentence)

# Display results
print("\n" + "-"*50)
print("Character Frequency:")
print("-"*50)
for char, count in sorted(frequency.items()):
    print(f"  '{char}': {count}")

print(f"\nTotal characters (excluding spaces): {sum(frequency.values())}")
print("-"*50)
