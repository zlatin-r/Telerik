array = [int(input()) for num in range(int(input()))]
array.sort()
count = 1
max_count = -9999
most_rep = 0

for i in range(len(array)):
    if i != len(array) - 1:
        if array[i] == array[i + 1]:
            count += 1
            if count > max_count:
                max_count = count
                most_rep = array[i]
        else:
            count = 1
            continue
    elif len(array) == 1:
        most_rep = array[0]
    else:
        break

print(most_rep)
