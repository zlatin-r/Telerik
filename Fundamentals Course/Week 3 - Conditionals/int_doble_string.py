v_type = input()

if v_type == "integer":
    variable = int(input())
    print(variable+1)
elif v_type == "real":
    variable = float(input())
    print(f"{variable+1:.2f}")
elif v_type == "text":
    variable = str(input())
    print(variable+"*")
