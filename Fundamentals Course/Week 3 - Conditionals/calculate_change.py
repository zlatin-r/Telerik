price = float(input())
paid = float(input())
change = (paid - price) * 100

if change >= 100:
    lev = change // 100
    change %= 100
    print(f"{int(lev)} x 1 lev")

if change >= 50:
    fifty = change // 50
    change %= 50
    print(f"{int(fifty)} x 50 stotinki")

if change >= 20:
    twenty = change // 20
    change %= 20
    print(f"{int(twenty)} x 20 stotinki")

if change >= 10:
    ten = change // 10
    change %= 10
    print(f"{int(ten)} x 10 stotinki")

if change >= 5:
    five = change // 5
    change %= 5
    print(f"{int(five)} x 5 stotinki")

if change >= 2:
    two = change // 2
    change %= 2
    print(f"{int(two)} x 2 stotinki")

if change >= 1:
    one = change // 1
    change %= 1
    print(f"{int(one)} x 1 stotinka")
