lines = int(input())
counter = 1
max_counter = 0
prev_number = 0

for i in range(lines):
    number = int(input())

    if number == prev_number:
        counter += 1
        if counter >= max_counter:
            max_counter = counter
    else:
        counter = 1
    prev_number = number

print(max_counter)

