text = input().split(" ")
result = []

for word in text:

    if word[0] in "aoueiAOUEI":
        word = word[1:] + word[0] + "che"
    else:
        word += "che"

    if len(word) % 2 == 1:
        word += "e"
    result.append(word)

print(" ".join(result))