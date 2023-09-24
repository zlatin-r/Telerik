num_spawn_points = int(input())
safe_houses = list(map(int, input().split()))

max_distance = 0

for i in range(num_spawn_points):
    distance = min([abs(i - s) for s in safe_houses])

    if distance > max_distance:
        max_distance = distance

print(max_distance)
