text = input()

for i in text:
    if i.isdigit():
        if i in text:
            try:
                result = int(text) + 1
            except:
                result = float(text) + 1
    else:
        result = text[::-1]

result = str(result)
