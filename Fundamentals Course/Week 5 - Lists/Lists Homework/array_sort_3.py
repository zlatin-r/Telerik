numbers = input().split(",")

zeros = []
others = []

for num in numbers:
    if num == "0":
        zeros.append(num)
    else:
        others.append(num)
others.extend(zeros)

print(",".join(others))