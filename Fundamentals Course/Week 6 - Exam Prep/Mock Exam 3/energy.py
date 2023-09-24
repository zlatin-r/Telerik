number = input()

sum_odd = 0
sum_even = 0

while True:

    for i in number:
        if int(i) % 2 == 0:
            sum_even += int(i)
        else:
            sum_odd += int(i)
    break

if sum_even > sum_odd:
    print(f"{sum_even} energy drinks")
elif sum_odd > sum_even:
    print(f"{sum_odd} cups of coffee")
elif sum_even == sum_odd:
    print(f"{sum_odd} of both")
