lines = int(input())
prev_number = int(input())
counter = 1
max_counter = 0

for num in range(lines-1):
    number = int(input())

    if number == prev_number:
        counter += 1
        if counter >= max_counter:
            max_counter = counter
    else:
        counter = 1

    prev_number = number

print(max_counter)
