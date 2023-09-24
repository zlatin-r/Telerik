lines = int(input())

vowels = "aouei"
best = 999
best_count = 0
result = ""

for _ in range(lines):
    food = input()
    length = len(food)
    count = 0

    for j in food:
        if j in vowels:
            count += 1

    ratio = count / length

    if ratio < best:
        best = ratio
        best_count = count
        result = food

    elif ratio == best:
        if count > best_count:
            best = ratio
            best_count = count
            result = food

        elif length > len(result):
            best = ratio
            best_count = count
            result = food

print(f'{result} {best_count}/{len(result)}')
