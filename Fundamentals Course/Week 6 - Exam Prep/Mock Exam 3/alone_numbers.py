lst = [int(x) for x in input().split(",")]
target = int(input())

for i in range(1, len(lst) - 1):

    if lst[i] == target and lst[i - 1] != target and lst[i + 1] != target:

        if lst[i - 1] > lst[i + 1]:
            lst[i] = lst[i - 1]
        elif lst[i] < lst[i + 1]:
            lst[i] = lst[i + 1]

print(lst)