array = [int(x) for x in input().split(", ")]
target = int(input())

for i in range(1, len(array) - 1):
    if array[i] == target and array[i - 1] != array[i] and array[i + 1] != array[i]:
        array[i] = max(array[i + 1], array[i - 1])

print(array)