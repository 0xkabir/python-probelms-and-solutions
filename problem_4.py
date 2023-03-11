# Write a program that generates a random number between 1 and 100 and asks the user to guess the number.

import random

random_number = random.randint(1, 100)
user_number = int(input("Guess an integer: "))

if random_number == user_number:
    print("Voila!! You guessed the correct number!")
else:
    print(f"You guessed the wrong number, the right one is {random_number}")