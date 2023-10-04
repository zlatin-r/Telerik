number = [int(x) for x in input()]
sum_even = 0
sum_odd = 0

for i in number:
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i

if sum_even > sum_odd:
    print(f"{sum_even} energy drinks")
elif sum_even < sum_odd:
    print(f"{sum_odd} cups of coffee")
else:
    print(f"{sum_even} of both")