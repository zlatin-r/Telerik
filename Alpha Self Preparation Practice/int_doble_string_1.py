type_input = input()
value = input()

if type_input == "integer":
    print(int(value)+1)
elif type_input == "real":
    print(f"{float(value)+1:.2f}")
else:
    print(value+"*")
