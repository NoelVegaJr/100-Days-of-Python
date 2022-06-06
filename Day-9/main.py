from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction program.")


bids = {}
auction_on = True

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
        

while auction_on:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    continue_bidding = input("Are there any other bidders? Type 'yes' or 'no'. ")
    
    if continue_bidding == 'no':
        auction_on = False
        find_highest_bidder(bids)
    elif continue_bidding == 'yes':
        clear()