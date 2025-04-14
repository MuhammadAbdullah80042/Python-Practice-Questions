# Q10: Create a number guessing game using a while loop. (USED AI FOR UNDERSTANDING SYNTAX)

import random
secret = random.randint(1, 100)
guess = None

print("Number Guessing Game: Guess the number between 1 and 100.")

while guess != secret:
    guess = int(input("Enter your guess: "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
print("Congratulations! You guessed the number:", secret)
