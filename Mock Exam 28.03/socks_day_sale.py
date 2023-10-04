budget = int(input())
price_pair = int(input())
discount = int(input())
threshold = int(input())

total_pairs = 0
change = 0

while budget >= price_pair:
    budget -= price_pair
    total_pairs += 1
    if price_pair - discount >= threshold:
        price_pair -= discount
    else:
        price_pair = threshold
if total_pairs >= 10:
    total_pairs += 1

change = budget

print(total_pairs, change)
