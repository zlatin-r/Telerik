for array in range(int(input())):
    new_array = input().split(" ")
    left_side = new_array[:len(new_array) // 2]

    if len(new_array) % 2 == 1:
        right_side = new_array[(len(new_array) // 2) + 1:]
    else:
        right_side = new_array[(len(new_array) // 2):]

    right_side_reversed = list(reversed(right_side))

    if right_side_reversed == left_side:
        print("Yes")
    else:
        print("No")
