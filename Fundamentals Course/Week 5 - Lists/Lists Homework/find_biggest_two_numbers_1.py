nums = [int(x) for x in input().split(' ')]
nums.sort(reverse=True)
nums = [str(x) for x in nums]

print(" ".join(nums[:2]))