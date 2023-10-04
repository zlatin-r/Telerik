lst1 = input().split(",")
lst2 = input().split(",")
result = []

for i in lst1:
    count = -1

    for j in lst2:
        count += 1

        if int(i) == int(j):

            for b in lst2[count + 1::]:

                if int(b) > int(j):
                    result.append(int(b))
                    break
                elif int(b) < int(j) or int(b) == int(j):
                    continue
                else:
                    result.append(-1)
                    count = -1
                    break

            else:
                result.append(-1)
            break

print(",".join(map(str, result)))
