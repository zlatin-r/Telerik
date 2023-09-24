lines = int(input())
sum_numbers = 0

for i in range(1, lines + 1):
    number = float(input())
    sum_numbers += number

print(f"{sum_numbers/lines:.2f}")
