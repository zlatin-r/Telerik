lst = input().split(",")
negative_lst = []
zero_lst = []
positive_lst = []

for i in lst:
    if int(i) < 0:
        negative_lst.append(i)
    elif int(i) == 0:
        zero_lst.append(i)
    else:
        positive_lst.append(i)

print(",".join(negative_lst + zero_lst + positive_lst))
