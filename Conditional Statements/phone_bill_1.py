total_texts = int(input())
total_minutes = int(input())

bill = 12
add_tax_price = 0
add_texts = 0
add_texts_price = 0
add_minutes = 0
add_min_price = 0

if total_minutes > 60:
    add_minutes = total_minutes - 60
    add_min_price = add_minutes * 0.10
    tax_min = add_min_price * 0.20

    add_tax_price += tax_min
    bill += add_min_price + tax_min

if total_texts > 20:
    add_texts = total_texts - 20
    add_texts_price = add_texts * 0.06
    tax_text = add_texts_price * 0.20

    add_tax_price += tax_text
    bill += add_texts_price + tax_text

print(f"{add_texts} additional messages for {add_texts_price:.2f} levas")
print(f"{add_minutes} additional minutes for {add_min_price:.2f} levas")
print(f"{add_tax_price:.2f} additional taxes")
print(f"{bill:.2f} total bill")