lst_1 = input().split(',')
lst_2 = input().split(',')
lst_3 = []
result = []

for i in range(len(lst_1)):

    if lst_1[i] in lst_2:
        lst_3.append((lst_2[lst_2.index(lst_1[(i)]):]))

for k in range(len(lst_3)):
    first_element = int(lst_3[k][0])

    for m in lst_3[k]:

        if int(m) > first_element:
            res = int(m)
            break
        else:
            res = -1

    result.append(res)

print(','.join(map(str, result)))
