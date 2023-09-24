number = input().split(" ")
negative = []
positive = []

for i in number:
    if int(i) >= 0:
        positive.append(i)
    else:
        negative.append(i)

print(" ".join(negative + positive))
