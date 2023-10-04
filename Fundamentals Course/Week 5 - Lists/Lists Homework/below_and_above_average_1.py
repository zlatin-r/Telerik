nums = [int(x) for x in input().split(",")]
average = (sum(nums) / len(nums))
below = []
above = []

for num in nums:
    if num < average:
        below.append(str(num))
    elif num == average:
        continue
    else:
        above.append(str(num))

print(f"avg: {average:.2f}")
print("below:", ",".join(below))
print("above:", ",".join(above))