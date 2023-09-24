N = int(input())
arr = [int(input()) for x in range(N)]
arr.sort()
count = 1
max_count = 0
most_freq = 0

for i in range(N - 1):
    if arr[i] == arr[i + 1]:
        count += 1
        if count >= max_count:
            max_count = count
            most_freq = arr[i]
    else:
        count = 1

print(f"{most_freq} ({max_count} times)")
