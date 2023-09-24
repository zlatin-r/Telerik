amount_texts = int(input())  # additional_min = 0.10
amount_minutes = int(input())  # #additional_text = 0.06
start_price = 12
additional_minutes_price = 0
additional_texts_price = 0
additional_minutes = 0
additional_texts = 0
additional_minutes_tax = 0
additional_texts_tax = 0

if amount_minutes > 60:
    additional_minutes = (amount_minutes - 60)
    additional_minutes_price = additional_minutes * 0.10
    additional_minutes_tax = additional_minutes_price * 0.20
if amount_texts > 20:
    additional_texts = (amount_texts - 20)
    additional_texts_price = additional_texts * 0.06
    additional_texts_tax = additional_texts_price * 0.20

taxes = additional_minutes_tax + additional_texts_tax
total_price = additional_minutes_price + additional_texts_price + start_price + taxes

print(f"{additional_texts} additional messages for {additional_texts_price:.2f} levas")
print(f"{additional_minutes} additional minutes for {additional_minutes_price:.2f} levas")
print(f"{taxes:.2f} additional taxes")
print(f"{total_price:.2f} total bill")
