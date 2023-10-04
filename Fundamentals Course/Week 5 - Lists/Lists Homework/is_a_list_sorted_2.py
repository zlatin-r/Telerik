lines = int(input())

for lst in range(lines):
    new_list = input().split(",")
    num_list = list(map(int, new_list))
    is_sorted = sorted(num_list)

    if num_list == is_sorted:
        print("true")
    else:
        print("false")
