numbers = input().split(" ")
nums = []

for i in numbers:
    nums.append(int(i))

nums = sorted(nums)
biggest = nums[-1]
second_biggest = nums[-2]

print(biggest, second_biggest)
