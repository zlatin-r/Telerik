N = int(input())
min_number = 9999999
max_number = -9999999
sum_number = 0

for i in range(1, N + 1):
    number = float(input())
    sum_number += number
    if number < min_number:
        min_number = number
    if number > max_number:
        max_number = number
print(f"min={min_number:.2f}")
print(f"max={max_number:.2f}")
print(f"sum={sum_number:.2f}")
print(f"avg={sum_number / N:.2f}")
