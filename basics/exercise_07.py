day = int(input("Write the day: "))
month = int(input("Write the month: "))

total_months = (month - 1) * 30
total = day + total_months

print(f"The total is {total} days")