d = int(input())
h = int(input())
m = int(input())
s = int(input())

sum_d = ((d * 24)*60)*60
sum_h = (h * 60)*60
sum_m = m * 60

sum_sec = sum_d + sum_h + sum_m + s

print(sum_sec)