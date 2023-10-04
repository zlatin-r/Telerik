numbers = [int(x) for x in input().split(' ')]

for i in range(len(numbers) - 1):
    while numbers[i] < numbers[i + 1]:
        peak_start = numbers[i]
