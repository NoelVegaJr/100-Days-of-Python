import random
options = ['Rock', 'Paper', 'Scissors']
player_response = input("What do you choose? Type Rock, Paper or Scissors\n")
computer_response = random.choice(options)

print(f"You picked {player_response}")
print(f"Computer picked {computer_response}")

player_won = True
is_tie = False
valid_response = True

if player_response not in options:
    valid_response = False

elif player_response == computer_response:
    is_tie = True

elif player_response == 'Rock':
    if computer_response == "Paper":
        player_won = False

elif player_response == 'Scissors':
    if computer_response == 'Rock':
        player_won = False

elif player_response == 'Paper':
    if computer_response == 'Scissors':
        player_won = False

if valid_response:
    if is_tie:
        print("It is a tie.")
    else:
        if player_won:
            print("You win!")
        else:
            print("You lose.")
else:
    print(f"\"{player_response}\" is an not a valid repsonse.")








