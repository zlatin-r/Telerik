n = int(input())
summ = 0
min_num = 99999999
max_num = -99999999

for num in range(n):
    number = float(input())
    summ += number

    if number < min_num:
        min_num = number
    if number > max_num:
        max_num = number

print(f"min={min_num:.2f}")
print(f"max={max_num:.2f}")
print(f"sum={summ:.2f}")
print(f"avg={summ/n:.2f}")
