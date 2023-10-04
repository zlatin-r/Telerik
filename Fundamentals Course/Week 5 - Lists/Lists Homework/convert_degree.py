lst = input().split(" ")
lst_F = []
F = 0
for i in lst:
    F = int(i) * 1.8 + 32
    lst_F.append(F)
    print(int(F))

