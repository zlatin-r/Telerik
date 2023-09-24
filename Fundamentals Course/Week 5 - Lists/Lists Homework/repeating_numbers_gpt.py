# Read the input
N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))

# Count the occurrences of each number
counts = [0] * 11  # Initialize an array to store the counts, indices represent numbers 1 to 10
for num in numbers:
    counts[num] += 1

# Find the most common number
max_count = 0
most_common_number = 1
for num in range(1, 11):
    if counts[num] > max_count:
        max_count = counts[num]
        most_common_number = num
    elif counts[num] == max_count and num < most_common_number:
        most_common_number = num

# Print the result
print(most_common_number)