lines = int(input())
elements = int(input())
lst = []

for i in range(lines):
    lst.append(int(input()))
    lst.sort()

summ = sum(lst[-elements:])
print(summ)
