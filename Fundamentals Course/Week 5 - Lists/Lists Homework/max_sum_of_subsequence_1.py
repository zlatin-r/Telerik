lines = int(input())
temp_sum = 0
max_sum = 0
lst = []


for i in range(lines):
    numbers = int(input())
    lst.append(numbers)
for num in lst:
    temp_sum += num
    if temp_sum < 0:
        temp_sum = 0
    if temp_sum > max_sum:
        max_sum = temp_sum
print(max_sum)