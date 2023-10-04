lst = input().split(",")
lst_zero = []
lst_nums = []

for i in lst:
    if int(i) == 0:
        lst_zero.append(i)
    else:
        lst_nums.append(i)

print(",".join(lst_nums + lst_zero))