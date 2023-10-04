# Read input
N = int(input())

# Print upper triangle
for i in range(1, N + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

# Print lower triangle
for i in range(N - 1, 0, -1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
