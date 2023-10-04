balanced_num = 0

while True:
    number = input()

    first_digit = int(number[0])
    second_digit = int(number[1])
    third_digit = int(number[2])

    if second_digit == first_digit + third_digit:
        balanced_num += int(number)
    else:
        print(balanced_num)
        break
