card_deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
card = input()
for i in card_deck:
    if i == card:
        break
    print(f'{i} of spades, {i} of clubs, {i} of hearts, {i} of diamonds')
print(f'{card} of spades, {card} of clubs, {card} of hearts, {card} of diamonds')
