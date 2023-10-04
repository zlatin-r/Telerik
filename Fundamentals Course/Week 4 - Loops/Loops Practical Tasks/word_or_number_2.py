lines = int(input())
summ = 0
words = "no words "

for i in range(lines):
    text = input()

    if text.isdigit():
        summ += eval(text)

    if text.isalpha():
        words = words.strip("no words ")
        words += text
        words += "-"

print(words.strip(words[-1]))
print(summ)
