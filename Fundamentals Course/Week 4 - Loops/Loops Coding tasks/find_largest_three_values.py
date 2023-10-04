N=int(input())
largest=-501
second_largest=-501
third_largest=-501
for i in range(N):
    num=int(input())
    if num>largest:
        third_largest=second_largest
        second_largest=largest
        largest=num
    elif num>second_largest:
        third_largest=second_largest
        second_largest=num
    elif num>third_largest:
        third_largest=num
print(f'{largest}, {second_largest} and {third_largest}')