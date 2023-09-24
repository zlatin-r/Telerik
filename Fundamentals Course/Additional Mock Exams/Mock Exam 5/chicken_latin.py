text = input().split(" ")
result = []

for word in text:
    prev = len(word)

    if word[0] in "aeiouAEIOU":
        new_word = word[1::]+word[0]+"che"
    if word[0] not in "aeiouAEIOU":
        new_word = word + "che"
    if len(word) % 2 == 0:
        new_word += "e"
    result.append(new_word)

print(" ".join(result))
