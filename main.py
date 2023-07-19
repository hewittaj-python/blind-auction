from art import logo
import os

# Variable declaration
all_bids = {}
auction_in_progress = True
highest_bid = {"name": "", "bid_amount": 0}

print(logo)
while auction_in_progress:
    name = input("What is your name? ")
    bid = float(input("What is your bid? $"))
    all_bids[name] = bid
    
    bids_closed = input("Would anyone else like to bid? (y/n) ")
    if bids_closed == 'y':
        os.system('clear')
    elif bids_closed == 'n':
        for name, bid in all_bids.items():
            if bid > highest_bid["bid_amount"]:
                highest_bid["name"] = name
                highest_bid["bid_amount"] = bid
        print(f"The highest bid was {round(highest_bid['bid_amount'], 2)} made by {highest_bid['name']}")
        break