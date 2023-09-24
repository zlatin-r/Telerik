N = int(input())
prev_number = 0
next_number = 0
result = ""

for i in range(N):
    number = int(input())
    next_number = number

    if i > 0:
        if prev_number > next_number:
            result += ">"
        elif prev_number < next_number:
            result += "<"
        elif prev_number == next_number:
            result += "="

    prev_number = next_number
    result += str(number)

print(result)
