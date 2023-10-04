number = input()
sum_digits = 0

for i in number:
    if i == "." or i == "-":
        continue
    sum_digits += int(i)

while sum_digits > 9:
    number = sum_digits
    sum_digits = 0

    for i in str(number):
        sum_digits += int(i)

print(sum_digits)