lines = int(input())
first_num = int(input())
result = str(first_num)

for i in range(lines - 1):
    next_num = int(input())

    if first_num == next_num:
        result += "=" + str(next_num)
    elif first_num > next_num:
        result += ">" + str(next_num)
    else:
        result += "<" + str(next_num)
    first_num = next_num

print(result)
