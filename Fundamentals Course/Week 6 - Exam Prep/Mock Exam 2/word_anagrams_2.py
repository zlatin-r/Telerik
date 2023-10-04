word = [x for x in input()]
lines = int(input())

for i in range(lines):
    anagrams = [y for y in input()]

    word.sort()
    anagrams.sort()

    if anagrams == word:
        print("Yes")
    else:
        print("No")
