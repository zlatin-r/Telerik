small_b = int(input())  # 1 liter
big_b = int(input()) * 5  # 5 liters
truck_c = int(input())

if big_b > truck_c:
    capacity_rest = truck_c - (truck_c // 5) * 5
else:
    capacity_rest = truck_c - big_b

if capacity_rest > small_b:
    print("-1")
elif capacity_rest < small_b:
    print(capacity_rest)
else:
    print(small_b)