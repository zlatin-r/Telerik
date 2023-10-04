english = input()
spanish = input()
result = ""

for i in range(max(len(english), len(spanish))):

    if i >= len(english):
        result += spanish[i]
    elif i >= len(spanish):
        result += english[i]
    elif english[i] == " " or spanish[i] == "-":
        result += " "
        continue
    elif english[i] == "-" or spanish[i] == " ":
        result += " "
        continue
    else:
        english_ord = ord(english[i]) - ord("a")
        spanish_ord = ord(spanish[i]) - ord("a")
        result_ord = abs(english_ord - spanish_ord)
        result += chr(result_ord + ord("a"))

print(result)
