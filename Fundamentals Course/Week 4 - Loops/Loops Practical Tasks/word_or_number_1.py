text = input()
result = 0

for i in text:
    if i.isdigit():
        result = eval(text) + 1
    else:
        result = text[::-1]

print(result)
