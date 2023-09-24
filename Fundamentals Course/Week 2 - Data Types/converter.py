MPG = int(input())

one_km = 1.6  # miles
one_gallon = 4.54  # liters

km = MPG * one_km  # gallon per km
lkm = one_gallon / km  # liter per km
l_per_100km = lkm * 100

print(f'{int(l_per_100km)} litres per 100 km')