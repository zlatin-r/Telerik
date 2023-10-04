line = input()

if line.isalpha():
    print(line[::-1])
elif "." in line:
    print(float(line) + 1)
else:
    print(int(line) + 1)