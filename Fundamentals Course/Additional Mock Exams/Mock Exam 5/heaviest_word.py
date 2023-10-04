n = int(input())
words = [input() for _ in range(n)]

summ = 0
max_value = -9999999
heaviest_word = ""

for word in words:
    for letter in word:
        letter_index = ord(letter.lower()) - 96

        summ += int(ord(letter.lower()) - 96)
        if summ >= max_value:
            max_value = summ
            heaviest_word = word
    summ = 0

print(max_value, heaviest_word)
