card = input()
deck = "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"
for i in deck:
    print(f"{i} of spades, {i} of clubs, {i} of hearts, {i} of diamonds")
    if i == card:
        break
