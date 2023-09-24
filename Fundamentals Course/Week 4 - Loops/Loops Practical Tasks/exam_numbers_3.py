start = int(input())
end = int(input())
target = int(input())

for i in range(start, end + 1):
    if i % 10 + (i // 10) % 10 + i // 100 == target:
        print(i)
