lines = int(input())
lst_1 = []
lst_2 = []

for i in range(lines):
    digits = int(input())
    lst_1.append(digits)
for j in range(lines):
    digits = int(input())
    lst_2.append(digits)

if lst_1 == lst_2:
    print("equal")
else:
    print("not equal")
