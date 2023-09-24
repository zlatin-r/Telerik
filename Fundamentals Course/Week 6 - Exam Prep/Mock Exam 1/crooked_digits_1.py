number = input().strip("-")
summ = 0
result = 0

while True:

    for i in number:
        if i == ".":
            continue
        summ += int(i)
        result = summ

    if result > 9:
        number = str(result)
        result = 0
        summ = 0
        continue
    else:
        break
print(result)
