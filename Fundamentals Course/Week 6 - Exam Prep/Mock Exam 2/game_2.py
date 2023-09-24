number = [int(x) for x in input()]

case1 = number[0] * number[1] * number[2]
case2 = number[0] + number[1] * number[2]
case3 = number[0] * number[1] + number[2]
case4 = number[0] + number[1] + number[2]

print(max(case1, case2, case3, case4))
