french_rolls = int(input("How many french rolls did you sell? "))
breads = int(input("How many breads did you sell? "))

total = french_rolls * 0.12 + breads * 1.50
save_money = total * 0.10

print(f"The amount of money that you can save from your work is R$ {save_money}")