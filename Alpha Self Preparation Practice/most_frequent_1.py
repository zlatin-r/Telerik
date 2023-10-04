lines = int(input())
lst = []
counter = 1
max_count = 0
most_freq = 0

for i in range(lines):
    lst.append(int(input()))
    lst.sort()

for j in range(len(lst)):
    if lst[j] == lst[j + 1]:
        counter += 1

        if counter >= max_count:
            max_count = counter
            most_freq = lst[j]
    else:
        counter = 1

    if j == len(lst) - 2:
        print(f"{most_freq}({max_count} times)")
        break
