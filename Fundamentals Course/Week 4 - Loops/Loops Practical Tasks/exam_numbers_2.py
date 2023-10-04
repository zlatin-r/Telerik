start = int(input())
end = int(input())
target = int(input())

for num in range(start, end + 1):
    sum = 0
    for digit in str(num):
        sum += int(digit)
    if sum == target:
        print(num)
