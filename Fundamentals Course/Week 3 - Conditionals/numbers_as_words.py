number = int(input())

ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

if 0 <= number <= 9:
    print(ones[number])
elif number == 10:
    print("ten")
elif 11 <= number <= 19:
    print(teens[number - 11])
elif 20 <= number <= 99:
    print(tens[number // 10 - 1] + " " + ones[number % 10])
elif 100 < number <= 999:
    first = number // 100
    second = (number // 10) % 10
    third = number % 10
    second_two = number % 100

    if second == 0 and third == 0:
        print(ones[first] + " hundred")
    elif third == 0:
        print(ones[first] + " hundred" + " and " + tens[number % 100 // 10 - 1])
    elif second == 0:
        print(ones[first] + " hundred" + " and " + ones[third])
    elif 10 < second_two < 20:
        print(ones[first] + " hundred" + " and " + teens[(number % 10) - 1])
    else:
        print(ones[number // 100] + " hundred" + " and " + tens[number % 100 // 10 - 1] + " " + ones[number % 10])
