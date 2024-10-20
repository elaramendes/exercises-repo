money_for_gasoline = float(input("How much money (in BRL) do you want to spend on gasoline? "))
price_of_gasoline = float(input("What's the price of gasoline? "))

total = money_for_gasoline / price_of_gasoline

print(f"You can put {total:.2f} liters of gasoline.")