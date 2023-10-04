lines = int(input())
counts = [0] * 11
most_rep = 1
max_count = 0

for i in range(lines):
    number = int(input())
    counts[number] += 1

for num in range(1, 11):

    if counts[num] > max_count:
        max_count = counts[num]
        most_rep = num
    elif counts[num] == max_count and num < most_rep:
        most_rep = num

print(most_rep)