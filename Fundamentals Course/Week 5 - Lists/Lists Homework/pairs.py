n = int(input())
lst = [int(el) for el in input().split(" ")]

x = False
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == n:
            print(",".join(str(el) for el in [lst[i], lst[j]]))
            x = True
if x is False:
    print("no pairs")
