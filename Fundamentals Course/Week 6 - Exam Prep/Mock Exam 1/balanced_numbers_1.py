result = 0

while True:
    number = input()

    if int(number[0]) + int(number[2]) == int(number[1]):
        result += int(number)
    else:
        print(result)
        break
