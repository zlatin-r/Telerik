a = float(input())
b = float(input())
c = float(input())

product = a * b * c

if product < 0:
    print("-")
elif product > 0:
    print("+")
else:
    print("0")