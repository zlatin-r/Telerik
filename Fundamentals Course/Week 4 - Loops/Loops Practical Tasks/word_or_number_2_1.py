lines = int(input())
text = ""
digits = 0

for i in range(lines):
    string = input()

    if string.isdigit():
        digits += int(string)

    if string.isalpha():
        text += string + "-"

if len(text) == 0:
    text = "no words "

print(text.strip(text[-1]))
print(digits)