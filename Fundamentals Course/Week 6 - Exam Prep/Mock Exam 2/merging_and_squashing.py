lines = int(input())
prev_number = input()
merged_numbers = []
squashed_numbers = []

for num in range(lines - 1):
    number = input()
    merged_number = prev_number[1] + number[0]
    merged_numbers.append(merged_number)

    middle = int(prev_number[1]) + int(number[0])
    if middle >= 10:
        middle = str(middle)
        middle = middle[1]

    squashed_number = prev_number[0] + str(middle) + number[1]
    squashed_numbers.append(squashed_number)
    prev_number = number

print(" ".join(merged_numbers))
print(" ".join(squashed_numbers))
