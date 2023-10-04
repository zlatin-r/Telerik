num = int(input())
result = []

for i in range(1, num + 1):
    if i % 3 == 0 or i % 7 == 0:
        continue
    result.append(str(i))

print(" ".join(result))