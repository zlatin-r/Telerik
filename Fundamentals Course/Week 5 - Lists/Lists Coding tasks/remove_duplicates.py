numbers = input().split(",")

my_set = []

for i in numbers:
    if i not in my_set:
        my_set.append(i)
print(",".join(my_set))
