month = input()
date = int(input())

if month == "March" and date >= 20 or month == "April" or month == "May" or month == "June " and date < 21:
    season = "Spring"

elif month == "June" and date >= 21 or month == "July" or month == "August" or month == "September" and date < 22:
    season = "Summer"

elif month == "September" and date >= 22 or month == "October" or month == "November" or month == "December" and date < 21:
    season = "Autumn"

else:
    season = "Winter"

print(season)
