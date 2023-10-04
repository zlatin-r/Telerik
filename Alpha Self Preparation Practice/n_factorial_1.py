numbers = [int(x) for x in range(1, int(input()) + 1)]
result = 1

for i in numbers:
    result = result * i

print(result)