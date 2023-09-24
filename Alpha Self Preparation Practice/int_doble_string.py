type_input = input()

if type_input == "real":
    variable = float(input()) + 1
    print(f"{variable:.2f}")

elif type_input == "integer":
    variable = int(input()) + 1
    print(variable)

elif type_input == "text":
    variable = input() + "*"
    print(variable)
