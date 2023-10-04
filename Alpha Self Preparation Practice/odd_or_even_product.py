n = int(input())
numbers = list(map(int, input().split()))

odd_product = 1
even_product = 1

for i in range(n):
    if i % 2 == 0:
        even_product *= numbers[i]
    else:
        odd_product *= numbers[i]

if odd_product == even_product:
    print("yes", odd_product)
else:
    print("no", even_product, odd_product)
