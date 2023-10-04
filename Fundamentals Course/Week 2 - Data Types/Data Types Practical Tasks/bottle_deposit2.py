half_liter_deposit=0.1
one_liter_deposit=0.25
num_bottles_half=int(input())*half_liter_deposit
num_bottles_one=int(input())*one_liter_deposit
total=num_bottles_half+num_bottles_one
print(f'{total: .2f}')
