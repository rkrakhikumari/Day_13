
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = int(bidding_record[bidder])
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name? ")
    price = int(input("What is your bid?$ "))
    bids[name] = price
    should_continue = input("Are there any bidders? Type 'yes' or 'no'.")
    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(bids)
    else:
        should_continue = "yes"