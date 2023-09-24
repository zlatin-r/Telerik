number = input()

first = int(number[0])
second = int(number[1])
third = int(number[2])

case_1 = first * second + third
case_2 = first + second * third
case_3 = first + second + third
case_4 = first * second * third

print(max(case_1, case_2, case_3, case_4))