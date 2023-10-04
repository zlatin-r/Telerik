MPG=int(input())
one_liter=4.54
one_km=1.6
km=MPG*one_km
litres=one_liter/km
LPK=litres*100
import math
print(math.floor(LPK), 'litres per 100 km')