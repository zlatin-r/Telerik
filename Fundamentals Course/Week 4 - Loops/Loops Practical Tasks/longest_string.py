longest_string = ""

while True:
    food = input()

    if food == "END":
        break
    elif len(food) >= len(longest_string):
        longest_string = food

print(longest_string)
