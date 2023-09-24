n = int(input())
max_number = -201
for v in range(n):
    next_number = int(input())
    if next_number > max_number:
        max_number = next_number
print(max_number)