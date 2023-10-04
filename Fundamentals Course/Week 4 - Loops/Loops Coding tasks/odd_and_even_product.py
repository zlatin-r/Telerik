N=int(input())
Odd_product=1
Even_product=1
for line in range(1,N+1):
    number=int(input())
    if line %2 == 1:
        Even_product=number*Even_product
    if line %2 ==0:
        Odd_product=number*Odd_product
if Even_product==Odd_product:
    print('yes', Odd_product)
else:
    print('no', Even_product, Odd_product)