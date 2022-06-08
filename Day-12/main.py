import atexit
import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
secret_number = random.randrange(1, 101)
difficulty = {'easy': 10, 'hard': 5}

chosen_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = difficulty[chosen_difficulty]


while True:
    
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess "))
    
    if guess > secret_number:
        print("Too high.")
    elif guess < secret_number:
        print("Too low")
    else:
        print(f"You found the secret number!")
        break
    
    attempts -= 1
    
    if attempts == 0:
        print(f"{secret_number} is the secret number.\nYou lose")
        break
