lst = [input().split(",") for _ in range(int(input()))]

for i in lst:
    i = [int(x) for x in i]

    if i == sorted(i):
        print("true")
    else:
        print("false")