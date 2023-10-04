n = int(input())
primes = []
result = ""

for num in range(1, n + 1):
    prime = True

    for i in primes:
        if num % i == 0 and i != 1:
            prime = False

    if prime:
        primes.append(num)
        result += "1"
        print(result)
    else:
        result += "0"

