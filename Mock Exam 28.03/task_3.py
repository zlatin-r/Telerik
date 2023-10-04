from datetime import datetime, timedelta

expected_blossom_date = input()

average_temp_prediction = int(input())
rain = int(input())
winter_length = int(input())

days_later = 0
days_earlier = 0
rain_more_or_less = 0

days_later += winter_length // 7

if average_temp_prediction > 20:
    days_earlier += average_temp_prediction - 20
elif 20 > average_temp_prediction:
    days_later += 20 - average_temp_prediction

if rain > 30:
    rain_more_or_less += rain - 30
    days_later += rain_more_or_less // 3

elif rain < 30:
    rain_more_or_less += 30 - rain
    days_later += rain_more_or_less // 3

days_total = days_later - days_earlier

if timedelta(days=days_total) > timedelta(days=1461):
    average_temp_prediction += 5

expected_blossom_date_str = datetime.strptime(expected_blossom_date, "%d"" ""%B"" ""%Y") + timedelta(days=days_total)

print(expected_blossom_date_str.strftime("%d %B %Y"))
