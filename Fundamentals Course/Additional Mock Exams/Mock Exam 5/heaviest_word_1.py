lines = int(input())
heaviest = ""
max_sum = 0
summ = 0

for _ in range(lines):
    word = input()

    for letter in word:
        summ += ord(letter.lower()) - 96
    if summ > max_sum:
        max_sum = summ
        heaviest = word
    summ = 0

print(max_sum, heaviest)



