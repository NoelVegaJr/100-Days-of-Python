import random
from art import logo


def deal():
    return random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] )

def user_hit_phase(hand):
    current_hand = hand
    score = sum(current_hand)
    if score > 21:
        if 11 in current_hand:
            current_hand.remove(11)
            current_hand.append(1)
            user_hit_phase(current_hand)
        return current_hand
    else:
        print(f"Your hand: {current_hand}")
        if input("Hit or Stay: ") == "hit":
            current_hand.append(deal())
            return user_hit_phase(current_hand)
        else:
            return current_hand


def computer_hit_phase(computer_hand, player_hand):
    player_score = sum(player_hand)
    computer_score = sum(computer_hand)
    while computer_score <= player_score:
        if computer_score == 21:
            return computer_hand
        
        print(computer_hand)
        print("computer hit")
        computer_hand.append(deal())
        computer_score = sum(computer_hand)
        
        
    
    return computer_hand


def blackjack():
    print(logo)
    user_cards = []
    computer_cards = []
    
    for _ in range(2):
        user_cards.append(deal()) 
        computer_cards.append(deal())

    print(f"Computers hand: {computer_cards[0]}")
    user_cards = user_hit_phase(user_cards)
    player_score  = sum(user_cards)
    
    if player_score > 21:
        print("You bust :(")
    else:   
        computer_cards = computer_hit_phase(computer_hand=computer_cards, player_hand=user_cards) 
        computer_score = sum(computer_cards)

        if computer_score > 21:
            print("You win!")
        elif player_score == computer_score:
            print("It's a tie.")
        else:
            print("You lose :(")
            
    print(f"Your hand: {user_cards}\nComputers hand: {computer_cards}")
    
    if input("\nDo you want to play again 'y' for yes and 'n' for no.\n") == "y":
        blackjack()

blackjack()