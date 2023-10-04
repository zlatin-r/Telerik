n = int(input())

for i in range(n):
    price = float(input())
    print(f"{price-(price*0.65):.2f}")