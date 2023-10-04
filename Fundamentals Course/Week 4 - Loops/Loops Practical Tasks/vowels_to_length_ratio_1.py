VOWELS = "aouei"

n = int(input())

best_word = ""
best_ratio = 1
best_vowels = 0

for _ in range(n):
    word = input()
    num_vowels = sum(1 for letter in word if letter in VOWELS)
    ratio = num_vowels / len(word)

    if ratio < best_ratio:
        best_word = word
        best_ratio = ratio
        best_vowels = num_vowels

    elif ratio == best_ratio:
        if num_vowels > best_vowels or (num_vowels == best_vowels and len(word) > len(best_word)):
            best_word = word
            best_vowels = num_vowels

print(f"{best_word}{best_vowels}/{len(best_word)}")
