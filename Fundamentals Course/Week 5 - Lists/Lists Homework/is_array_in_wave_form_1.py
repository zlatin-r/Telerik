arr = [int(x) for x in input().split(' ')]
res = "yes"

for i in range(1, len(arr) - 1):
    if not arr[i - 1] < arr[i] > arr[i + 1] and not arr[i - 1] > arr[i] < arr[i + 1]:
        res = "no"
        break
print(res)