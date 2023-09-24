numbers = input().split(", ")
nums = []
str_nums = []

for i in numbers:
    nums.append(int(i))

nums = sorted(nums)
nums.reverse()

for i in nums:
    str_nums.append(str(i))

print(", ".join(str_nums))
