X = int(input())
Y = int(input())
Z = int(input())

for i in range(X, Y + 1):
    last = i % 10
    second = i // 10 % 10
    first = i // 100
    if first + second + last == Z:
        print(i)