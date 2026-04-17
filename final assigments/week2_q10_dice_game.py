'''
Dice Guessing Game
Computer generates random dice value (1-6)
Player guesses the value
Shows emoji based on guess accuracy
'''

import random

# Function to show face emoji
def show_face(dice_value, guess):
    if dice_value == guess:
        return "😊 SMILING FACE - Correct guess!"
    elif abs(dice_value - guess) == 1:
        return "😐 NEUTRAL FACE - Off by 1"
    else:
        return "😢 SAD FACE - Wrong guess"

# Main program
print("="*50)
print("DICE GUESSING GAME")
print("="*50)
print("Dice values: 1 to 6")
print("Guess the dice value!\n")

# Generate random dice value
dice_value = random.randint(1, 6)

# Get player guess
try:
    guess = int(input("Enter your guess (1-6): "))
    
    # Validate input
    if guess < 1 or guess > 6:
        print("Invalid! Please enter a number between 1 and 6")
    else:
        # Show result
        print("\n" + "="*50)
        print(f"Dice rolled: {dice_value}")
        print(f"Your guess:  {guess}")
        print("-"*50)
        print(show_face(dice_value, guess))
        print("="*50)

except ValueError:
    print("Invalid input! Please enter a valid number.")
