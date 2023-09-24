lines = int(input())
first_number = input()
merged = []
squashed = []

for num in range(lines - 1):
    next_number = input()

    merged.append(first_number[1] + next_number[0])

    middle = int(first_number[1]) + int(next_number[0])
    if middle >= 10:
        middle -= 10
    squashed.append(first_number[0] + str(middle) + next_number[1])

    first_number = next_number

print(" ".join(merged))
print(" ".join(squashed))