n = int(input())
temp = 0
max_sum = 0

for i in range(n):
    number = int(input())
    temp += number
    if temp < 0:
        temp = 0
    if temp > max_sum:
        max_sum = temp
print(max_sum)
