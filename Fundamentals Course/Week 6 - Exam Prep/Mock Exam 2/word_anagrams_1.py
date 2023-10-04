word = [str(el) for el in input()]
word.sort()
lines = int(input())

for i in range(lines):
    next_word = [str(el) for el in input()]
    next_word.sort()

    if word == next_word:
        print("Yes")
    else:
        print("No")