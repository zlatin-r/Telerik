food = ''
max_len_food = ''

while food != 'END':
    food = input()

    if len(food) >= len(max_len_food) and food != 'END':
        max_len_food = food

print(max_len_food)
