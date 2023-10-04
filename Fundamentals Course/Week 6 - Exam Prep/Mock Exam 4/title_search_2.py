title = input()

for _ in range(int(input())):
    new_input = input()
    new_word = ''

    for i in title:

        if new_input != '' and i == new_input[0]:
            new_input = new_input[1:]
        else:
            new_word += i

    if new_input == '':
        title = new_word
        print(title)
    else:
        print("No such title found!")
