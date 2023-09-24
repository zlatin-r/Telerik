time = input().strip()
result = "invalid time"

if (time[-9:-6]).isdigit() and (time[-5:-3]).isdigit():

    if time[-2:] == 'PM':
        try:
            if 11 >= int(time[0:2]) >= 10:
                result = "beer time"
            elif (int(time[0:2])) == 12:
                result = "non-beer time"
        except:
            if 9 >= int(time[0]) >= 1:
                result = "beer time"

    if time[-2:] == 'AM':
        try:
            if int(time[0:2]) == 12:
                result = "beer time"
            elif 12 >= int(time[0:2]) >= 10:
                result = "non-beer time"
        except:
            if 2 >= int(time[0]) >= 1:
                result = "beer time"
            elif 9 >= int(time[0]) >= 3:
                result = "non-beer time"

else:
    result = "invalid time"

print(result)
