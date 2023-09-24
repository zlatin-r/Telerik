HY = int(input())
DY = 0

if HY <= 2:
    DY = HY * 10
else:
    DY = 20 + (4 * (HY - 2))

print(DY)
