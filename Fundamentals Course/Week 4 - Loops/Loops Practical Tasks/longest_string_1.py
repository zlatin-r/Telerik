food = ''
max_len_food = ''

while True:
    food = input()

    if food == 'END':
        break
    if len(food) >= len(max_len_food):
        max_len_food = food

print(max_len_food)
