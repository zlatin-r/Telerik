target = int(input())
lines = int(input())
average = 0

for i in range(lines):
    word = input()
    summ = 0

    for j in word:
        summ += ord(j) - 96
    distance = target - summ
    average += abs(distance)

    print(word, abs(distance))
print(f"{average / lines:.2f}")
