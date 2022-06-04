import random
from hangman_art import logo, stages
from hangman_words import word_list

chosen_word = random.choice(word_list)
display = []
guesses = []
turns = 6

for letter in chosen_word:
    display.append("_")
    
while True:
    print(logo)
    print(stages[turns])
    print(f"Letters already guessed: {', '.join(guesses)}")
    print(f"{turns} chances remaining.")

    correct_guess = False
    
    if turns == 0:
        print(stages[turns])
        print("You lose.")
        print(f"\"{chosen_word}\" is the answer.")
        break
    elif "_" not in display:
        print("You won!")
        break
        
    print(" ".join(display), "\n")    
    guess = input("Guess a letter: ").lower()
    
    if guess in guesses:
        print(f"Already picked \"{guess}\", please choose another letter.")
        continue
    else:
        guesses.append(guess)

        if guess in chosen_word:
            for index, letter in enumerate(chosen_word):
                if guess == letter:
                    correct_guess = True
                    display[index] = letter
        else:
            turns -= 1   
            



        

    
    





