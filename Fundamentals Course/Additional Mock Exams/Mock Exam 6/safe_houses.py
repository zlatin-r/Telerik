import math

spawn_points = int(input())
save_houses = [int(house) for house in input().split(" ")]
save_houses.sort()
result = []
res = 0
counter = 0
max_count = 0

for point in range(spawn_points):

    if point in save_houses:
        result.append("S")
    else:
        result.append("x")

for i in result:
    if len(save_houses) < 2:
        if i == "x":
            counter += 1
            if counter >= max_count:
                max_count = counter
                res = counter
        else:
            counter = 0
            continue
    else:
        if i == "x":
            counter += 1
            if counter >= max_count:
                max_count = counter
                res = counter

        elif i == "S":
            counter = 0
            res = max_count / 2

print(math.ceil(res))
