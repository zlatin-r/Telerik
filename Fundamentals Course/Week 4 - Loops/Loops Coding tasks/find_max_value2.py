n=int(input())
max_num=-200
for i in range(1,n+1):
    num=int(input())
    if num >= max_num:
        max_num=num
print(max_num)