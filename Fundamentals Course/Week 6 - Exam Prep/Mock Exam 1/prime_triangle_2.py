new_input = input()

prime_numbers = []
result = ''

for i in range(1, int(new_input) + 1):
    is_prime = True

    for j in prime_numbers:
        if j != 1 and i % j == 0:
            is_prime = False

    if is_prime:
        prime_numbers.append(i)
        result += "1"
        print(result)
    else:
        result += '0'
        