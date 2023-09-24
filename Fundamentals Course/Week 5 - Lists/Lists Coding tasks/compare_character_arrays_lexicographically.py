first_array = list(input())
second_array = list(input())

if first_array < second_array:
    result = "first"
elif first_array > second_array:
    result = "second"
else:
    result = "equal"

print(result)
