n = int(input())
x = float(input())
s = 1
k = 1
factorial = 1
for i in range(1, n + 1):
    factorial = factorial*i
    s = s + (factorial / x ** k)
    k = k + 1
    if k == n + 1:
        break
print(f'{s:.5f}')