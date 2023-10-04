A = float(input())
B = float(input())
value_a = A
value_b = B

if A > B:
    A = value_b
    B = value_a
print(f"{A:g} {B:g}")
