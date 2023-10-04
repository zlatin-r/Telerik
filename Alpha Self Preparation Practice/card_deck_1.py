card = input()
deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

for i in deck:
    if i != card:
        print(f"{i} of spades, {i} of clubs, {i} of hearts, {i} of diamonds")
    else:
        print(f"{i} of spades, {i} of clubs, {i} of hearts, {i} of diamonds")
        break
