# Number guessing game in Python

import random

# Generate a random number between 1 and 100
target = random.randint(1, 100)

# Initialize the player's guess to 0
guess = 0

# Initialize the number of guesses the player has made
num_guesses = 0

# Game loop
while guess != target:
    # Get the player's guess
    guess = int(input("Guess a number between 1 and 100: "))

    # Increment the number of guesses the player has made
    num_guesses += 1

    # Check if the player's guess is too low or too high
    if guess < target:
        print("Your guess is too low. Try again.")
    elif guess > target:
        print("Your guess is too high. Try again.")

# Tell the player they have won
print(f"Congratulations, you guessed the number in {num_guesses} guesses!")
