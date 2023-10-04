N = int(input())
K = int(input())
arr = [int(input()) for i in range(N)]
arr.sort()

print(sum(arr[-K:]))
