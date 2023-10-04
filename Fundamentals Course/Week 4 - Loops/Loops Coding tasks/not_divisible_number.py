N = int(input())
for num in range(1, N + 1):
    if num % 3 != 0:
        if num % 7 != 0:
            print(num, end=' ')
