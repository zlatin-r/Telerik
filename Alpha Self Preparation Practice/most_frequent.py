N = int(input())
arr = []
counter = 1
max_count = 0
prev_i = 0
most_freq = 0

for i in range(N):
    arr.append(int(input()))
    arr.sort()

for i in arr:
    if i == prev_i:
        counter += 1
        if counter > max_count:
            max_count = counter
            most_freq = i
    else:
        counter = 1

    prev_i = i
print(f"{most_freq}({max_count}times)")
