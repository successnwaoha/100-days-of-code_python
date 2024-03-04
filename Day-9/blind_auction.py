from os import system
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)
bids = {}
continue_bidding = True

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of: ${highest_bid}")
  
while continue_bidding:
  name = input("What is your name?: ")
  price = int(input("How much are you bidding? $"))
  bids[name] = price
  should_continue = input("Are there any other bidders?: Type 'yes' or 'no'.: ")
  if should_continue == "no":
    continue_bidding = False
    find_highest_bidder(bids)
  elif should_continue == "yes":
    system('cls')