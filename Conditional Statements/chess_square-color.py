l=input()
r=int(input())
if l == 'a'or l=='c'or l=='e'or l=='g':
    if r %2==0:
        print('light')
    else:
        print('dark')
else:
    if r % 2 == 0:
        print('dark')
    else:
        print('light')