l = input()
r = int(input())

if r % 2 == 1 and (l == "a" or l == "c" or l == "e" or l == "g"):
    print("dark")
elif r % 2 == 0 and (l == "b" or l == "d" or l == "f" or l == "h"):
    print("dark")
else:
    print("light")
