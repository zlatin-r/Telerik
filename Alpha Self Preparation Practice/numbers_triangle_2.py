n = int(input())  # number of rows in the pyramid

for i in range(1, n+1):
    row = list(range(1, i+1))
    print(*row)  # print the current row

for i in range(n-1, 0, -1):
    row = list(range(1, i+1))
    print(*row)  # print the current row
