moves = input()
x, y = 0, 0

for i in moves:
    if i == "R":
        x += 1
    elif i == "L":
        x -= 1
    elif i == "U":
        y += 1
    elif i == "D":
        y -= 1

print((x, y))