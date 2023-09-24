logs = int(input())
result = 0

while logs > 0:
    result += 1
    logs -= result

    if logs < result + 1:
        break

print(result)