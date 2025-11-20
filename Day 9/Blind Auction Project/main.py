# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo

print(logo)
store = {}
def highest_bidder():
    while True:
        name = input("What is your name?\n>> ")
        bid = int(input("What is your bid?\n>> $"))
        store[name] = bid
        if input("Are there any other bidders? Type 'Yes' or 'No'\n>> ").lower() == "yes":
            print("\n" * 30)
            continue
        else:
            break
    number = 0
    winner = ""
    for item in store:
        if store[item] > number:
            number = store[item]
            winner = item

    print(f"{winner} made the highest bid of ${number}.")

highest_bidder()


