price = float(input())
paid = int(input())
change = (paid - price) * 100

if change >= 100:
    coins = change // 100
    change -= coins * 100
    print(f"{int(coins)} x 1 lev")
if change >= 50:
    coins = change // 50
    change -= coins * 50
    print(f"{int(coins)} x 50 stotinki")
if change >= 20:
    coins = change // 20
    change -= coins * 20
    print(f"{int(coins)} x 20 stotinki")
if change >= 10:
    coins = change // 10
    change -= coins * 10
    print(f"{int(coins)} x 10 stotinki")
if change >= 5:
    coins = change // 5
    change -= coins * 5
    print(f"{int(coins)} x 5 stotinki")
if change >= 2:
    coins = change // 2
    change -= coins * 2
    print(f"{int(coins)} x 2 stotinki")
if change >= 1:
    coins = change // 1
    change -= coins * 1
    print(f"{int(coins)} x 1 stotinka")
