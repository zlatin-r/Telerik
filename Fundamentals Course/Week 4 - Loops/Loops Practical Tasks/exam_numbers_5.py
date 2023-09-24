start = int(input())
end = int(input())
target = int(input())

for num in range(start, end+1):
    num = str(num)
    if int(num[0]) + int(num[1]) + int(num[2]) == target:
        print(num)