time = input()

time_format = time[:-3]
tt_format = time[-2:]
hour = time[:-6]
minutes = time[-5:-3]

if hour.isdigit() and minutes.isdigit():

    if tt_format == "PM":
        print('beer time') if int(hour) != 12 else print('non-beer time')
    elif tt_format == "AM":
        print('non-beer time') if 3 <= int(hour) <= 11 else print('beer time')
    else:
        print('invalid time')

else:
    print('invalid time')
