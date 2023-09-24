HY = int(input())

if HY <= 2:
    print(HY * 10)
else:
    remaining_years = HY - 2
    print((remaining_years * 4) + 20)

