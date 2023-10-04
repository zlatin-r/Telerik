count_nums = int(input())

max_num = -201

for i in range(1, count_nums + 1):
    number = int(input())
    if number > max_num:
        max_num = number
print(max_num)
