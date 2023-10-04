lines = int(input())
my_list = []
prev_num = 0
counter = 1
max_counter = 0

for i in range(lines):
    my_list.append(input())

for num in my_list:
    if num == prev_num:
        counter += 1
        if counter >= max_counter:
            max_counter = counter
    else:
        counter = 1
    prev_num = num

print(max_counter)