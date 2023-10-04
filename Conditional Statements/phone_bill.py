start_price = 12.00
total_texts = int(input())
total_min = int(input())

add_texts_price = (total_texts - 20) * 0.06
add_min_price = (total_min - 60) * 0.10
add_texts_tax = add_texts_price * 0.20
add_min_tax = add_min_price * 0.20

if total_texts > 20:
    print(total_texts - 20, 'additional messages for', f'{add_texts_price:.2f} levas')
else:
    add_texts_price = 0
    add_texts_tax = 0
    print('0 additional messages for 0.00 levas')

if total_min > 60:
    print(total_min - 60, 'additional minutes for', f'{add_min_price:.2f} levas')
else:
    add_min_price = 0
    add_min_tax = 0
    print('0 additional minutes for 0.00 levas')

total_taxes = add_texts_tax + add_min_tax
total_bill = start_price + add_texts_price + add_texts_tax + add_min_price + add_min_tax

print(f'{total_taxes:.2f} additional taxes')
print(f'{total_bill:.2f} total bill')
