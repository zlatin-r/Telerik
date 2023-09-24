N = int(input())
lst = [int(x) for x in input().split(" ")]

for i in range(N):
    if lst[i-1] < lst[i] > lst[i+1]:
        print(i)
        break
else:
    print("-1")

