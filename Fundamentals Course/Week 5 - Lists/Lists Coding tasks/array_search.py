line = input().split(",")

result = []

for i in range(1, len(line) + 1):
    if str(i) not in line:
        result.append(str(i))

print(",".join(result))
