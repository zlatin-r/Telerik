numbers = input().split(",")

for i in numbers:
    if i == "0":
        numbers.remove(i)
        numbers.append(i)

print(",".join(numbers))
