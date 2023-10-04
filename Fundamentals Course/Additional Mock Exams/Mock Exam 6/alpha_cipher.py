numbers = [input() for _ in range(5)]
result = []

for num in numbers:

    product = int(num[0]) * int(num[1]) * int(num[2])
    product = str(product)
    result.append(product[-1])

print("".join(result))
