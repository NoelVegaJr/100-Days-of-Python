import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']




word_list = ["strawberry", "friendship", "everything", "appreciate", "motivation", "detonation", "credential", "recolonize", "disability", "expiration"]
chosen_word = random.choice(word_list)

display = []
turns = 6

for letter in chosen_word:
    display.append("_")
    
end_of_game = False

while not end_of_game:
    print(stages[turns])
    print(" ".join(display), "\n")
    correct_guess = False
    guess = input("Guess a letter: ").lower()
    for index, letter in enumerate(chosen_word):
        if guess == letter:
            correct_guess = True
            display[index] = letter

    if not correct_guess:
        turns -= 1
        print(f"Wrong guess. {turns} guesses left.")
    else:
        print("Good guess!")
        
    if turns == 0:
        print(stages[turns])
        print("You lose.")
        print(f"\"{chosen_word}\" is the answer.")
        end_of_game = True
    elif "_" not in display:
        print("\n", " ".join(display))
        print("You won!")
        end_of_game = True
    
    





