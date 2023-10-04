l1 = [int(x) for x in input().split(',')]
l2 = [int(x) for x in input().split(',')]
l3 = []
result = []

for x in range(len(l1)):
    for y in range(len(l2)):

        if l1[x] == l2[y]:
            l3.append(l2[y + 1:])

            if len(l3[0]) > 0:
                for i in range(len(l3[0])):

                    if l3[0][i] > l1[x]:
                        result.append(l3[0][i])
                        l3.clear()
                        break

                else:
                    result.append(-1)
                    l3.clear()
            else:
                result.append(-1)
                l3.clear()

print(*result, sep=",")