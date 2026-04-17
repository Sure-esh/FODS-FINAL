'''
Number Guessing Game
Computer generates random number 1-50, user has max 7 attempts
'''

import random

# Game variables
secret_number = random.randint(1, 50)
attempts = 0
max_attempts = 7
guessed_correctly = False

print("="*50)
print("NUMBER GUESSING GAME")
print("="*50)
print("I'm thinking of a number between 1 and 50.")
print(f"You have {max_attempts} attempts to guess it!")
print("="*50 + "\n")

# Game loop
while attempts < max_attempts:
    try:
        # Get user input
        guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
        
        # Validate input
        if guess < 1 or guess > 50:
            print("Please enter a number between 1 and 50!")
            continue
        
        attempts += 1
        
        # Check the guess
        if guess == secret_number:
            guessed_correctly = True
            print("\n" + "="*50)
            print("🎉 CONGRATULATIONS! 🎉")
            print(f"You guessed correctly! The number was {secret_number}")
            print(f"You took {attempts} attempts")
            print("="*50)
            break
        
        elif guess < secret_number:
            print(f"❌ Too low! Try a higher number.")
            remaining = max_attempts - attempts
            print(f"Remaining attempts: {remaining}\n")
        
        else:  # guess > secret_number
            print(f"❌ Too high! Try a lower number.")
            remaining = max_attempts - attempts
            print(f"Remaining attempts: {remaining}\n")
    
    except ValueError:
        print("Invalid input! Please enter a valid number.\n")

# Game over message
if not guessed_correctly:
    print("\n" + "="*50)
    print("Better luck next time!")
    print(f"The secret number was: {secret_number}")
    print("="*50)
