small_b = int(input())
big_b = int(input()) * 5
truck_c = int(input())
result = ""

if big_b == truck_c:
    result = "0"
elif big_b > truck_c:
    result = truck_c % 5
    if result > small_b:
        result = "-1"
elif big_b + small_b < truck_c:
    result = "-1"
else:
    result = truck_c - big_b

print(result)