my_list = [input() for _ in range(int(input()))]

count = 1
max_count = 1

for i in range(len(my_list) - 1):
    if my_list[i] == my_list[i + 1]:
        count += 1
    else:
        count = 1
    if count > max_count:
        max_count = count

print(max_count)
