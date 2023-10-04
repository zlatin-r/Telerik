targets = int(input())

Gs = int(input()) * targets
Gl = int(input()) * 2
Ps = int(input()) * targets
Pl = int(input()) * 2

if Gs + Gl < Ps + Pl:
    print("George")
elif Gs + Gl > Ps + Pl:
    print("Peter")
else:
    print("Draw")