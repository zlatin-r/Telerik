half_lit_dep = 0.1
one_lit_dep = 0.25

half_lit_bottles = int(input())
one_lit_bottles = int(input())

sum_half_lit = half_lit_dep*half_lit_bottles
sum_one_lit = one_lit_dep*one_lit_bottles
total_sum = sum_half_lit + sum_one_lit
print(f'{total_sum:.2f}')

