N = int(input())

for i in range(1, N + 1):
    item_price = float(input())
    discount = item_price - (item_price * 0.65)
    print(f"{discount:.2f}")
