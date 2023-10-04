alphabet = " abcdefghijklmnopqrstuvwxyz"
target_number = int(input())
count_words = int(input())
sum_number = 0
distance_number = 0
average = 0

for i in range(count_words):
    word = input()
    for letter in word:
        if letter in alphabet:
            sum_number += alphabet.index(letter)
    distance_number = sum_number - target_number
    print(word, abs(distance_number))
    average += abs(distance_number)
    sum_number = 0

print(f"{average/count_words:.2f}")