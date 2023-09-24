numbers = input().split(",")

average = 0
below = []
above = []

for i in numbers:
    average += int(i)
average /= len(numbers)

for i in numbers:
    if int(i) < average:
        below.append(i)
    elif int(i) > average:
        above.append(i)

print(f"avg: {average:.2f}")
print("below:", ",".join(below))
print("above:", ",".join(above))
