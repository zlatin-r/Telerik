numbers = input().split(",")
negative = []
positive = []
zero = []

for i in numbers:

    if int(i) < 0:
        negative.append(i)
    elif int(i) > 0:
        positive.append(i)
    elif int(i) == 0:
        zero.append(i)

print(",".join(negative + zero + positive))
