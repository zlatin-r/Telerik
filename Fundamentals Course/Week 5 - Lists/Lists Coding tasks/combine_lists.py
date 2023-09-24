list_1 = input().split(",")
list_2 = input().split(",")
list_3 = []

for i in range(len(list_1)):
    list_3.append(list_1[i])
    list_3.append(list_2[i])

print(",".join(list_3))

