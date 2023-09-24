human_years = int(input())

if human_years <= 2:
    print(human_years * 10)
else:
    remaining_years = human_years - 2
    print(remaining_years * 4 + 20)
