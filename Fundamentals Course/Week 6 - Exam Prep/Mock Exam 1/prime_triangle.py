init_number = int(input())

my_list = [1]

for number in range(init_number + 1):
    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        my_list.append(number)

for prime_num in my_list:
    for number in range(1, prime_num + 1):
        if number in my_list:
            print(1, end="")
        else:
            print(0, end="")
    print()
