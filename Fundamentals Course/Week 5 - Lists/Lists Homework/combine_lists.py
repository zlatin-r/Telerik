lst1 = input().split(',')
lst2 = input().split(',')

lst3 = []

for i in range(len(lst1)):
    lst3.append(lst1[i])
    lst3.append(lst2[i])

output = ",".join(lst3)
print(output)