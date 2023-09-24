lst = [input() for _ in range(5)]
result = ""

for i in range(len(lst)):
    summ = int(lst[i][0]) * int(lst[i][1]) * int(lst[i][2])
    result += str(summ % 10)

print(result)