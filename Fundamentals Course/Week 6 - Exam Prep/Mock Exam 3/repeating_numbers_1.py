numbers = [int(input()) for x in range(int(input()))]
numbers.sort()
count = 1
max_count = 0
max_rep = 0

if len(numbers) > 1:
    for el in range(len(numbers) - 1):

        if numbers[el] == numbers[el + 1]:
            count += 1
        else:
            count = 1

        if count > max_count:
            max_count = count
            max_rep = numbers[el]

else:
    max_rep = numbers[0]
print(max_rep)