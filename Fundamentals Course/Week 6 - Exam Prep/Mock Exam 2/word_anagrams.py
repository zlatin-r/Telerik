w = input()

n = int(input())

word_list = []

for i in range(n):
    list_words = input()
    word_list.append(list_words)

word = sorted(w)

for anagram in word_list:
    if word == sorted(anagram):
        print("Yes")
    else:
        print("No")