my_list = input().split(",")
rotation = int(input())

for _ in range(rotation):
    my_list = my_list[1:] + [my_list[0]]

print(",".join(my_list))