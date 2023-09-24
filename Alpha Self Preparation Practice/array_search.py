numbers = list(map(int, input().split(",")))
output_numbers = []

for i in range(1, len(numbers) + 1):
    if i not in numbers:
        output_numbers.append(str(i))

print(",".join(output_numbers))
