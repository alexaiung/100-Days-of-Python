#from art import art
#print(art)

def find_highest_bidder(bids_dict):
    winner_name = ""
    winner_bid = 0
    for name, bid in bids_dict.items():
        if bid > winner_bid:
            winner_bid = bid
            winner_name = name
    return winner_name, winner_bid

print("Welcome to the secret auction program.")

bids = dict()
more_bidders = True
while more_bidders:
    last_name = ""
    name = ""
    bid = ""
    keep_going = ""
    while not name.isalpha():
        name = input("What's your name? ")
        if not name.isalpha():
            print('Invalid name, please try again.')
    while not bid.isdecimal():
        bid = input("What's your bid? $")
        if not bid.isdecimal():
            print('Invalid value, please try again.')
    bid = float(bid)
    bids[name] = bid
    if keep_going not in ['yes', 'no']:
        keep_going = input('Are there any other bidders? Type "yes" or "no": ').lower()
        if keep_going not in ['yes', 'no']:
            print('Invalid answer, please try again.')
        if keep_going == 'no':
            more_bidders = False


winner_name, winner_bid = find_highest_bidder(bids)
print(f'The winner is {winner_name.capitalize()} with a bid of ${winner_bid}')
