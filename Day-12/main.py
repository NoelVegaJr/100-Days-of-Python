import atexit
import random
from art import logo


def new_guess():
    return int(input("Make a guess: "))


def check_guess(guess, answer, turns):
    if guess == answer:
        print("You guessed right, you win!")
    else:
        if guess > answer:
            print("Too high.")
        else:
            print("Too low")

        return turns - 1


def set_difficulty():
    diff = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if diff == 'easy':
        return 10
    else:
        return 5
    

def number_guessing_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    secret = random.randrange(1, 101)
    turns = set_difficulty() 

    while True:
        
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = new_guess()
        turns = check_guess(guess, secret, turns)
        
        if turns == 0:
            print("You've run out of guesses, you lose :(")
            return
        elif guess != secret:
            print("Guess again")
        else:
            return
    
number_guessing_game()