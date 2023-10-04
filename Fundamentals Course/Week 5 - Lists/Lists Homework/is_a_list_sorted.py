lines = int(input())

for _ in range(lines):
    lst = list(map(int, input().split(",")))

    print("true") if lst == sorted(lst) else print("false")