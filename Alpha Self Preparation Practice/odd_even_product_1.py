N = int(input())
arr = list(map(int, input().split()))
odd = 1
even = 1

for i in range(N):
    if i % 2 == 0:
        even *= arr[i]
    else:
        odd *= arr[i]
if even == odd:
    print("yes", even)
else:
    print("no", even, odd)
