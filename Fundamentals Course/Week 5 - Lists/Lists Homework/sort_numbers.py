numbers = input().split(",")

listIntNumbers = list(map(int, numbers))

sortedNumbers = sorted(listIntNumbers, reverse=True)

print(*sortedNumbers, sep=", ")
