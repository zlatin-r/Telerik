N = int(input())
num = 0
for i in range(1, N+1):
    value=float(input())
    num += value
print(f'{(num/N):.2f}')