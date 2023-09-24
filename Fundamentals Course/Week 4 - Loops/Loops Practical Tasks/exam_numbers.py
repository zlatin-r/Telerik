x_start = int(input())
y_end = int(input())
target = int(input())
sum_of_digits = 0

for numbers in range(x_start, y_end + 1):
    numbers = str(numbers)

    digit1 = int(numbers[0])
    digit2 = int(numbers[1])
    digit3 = int(numbers[2])

    sum_of_digits = digit1 + digit2 + digit3

    if sum_of_digits == target:
        print(numbers)
