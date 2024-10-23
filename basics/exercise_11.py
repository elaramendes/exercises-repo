days = int(input("How many days without accident? "))

year = days // 365
remaining = days % 365
month = remaining // 30
days_left = remaining % 30

print(f"{year} year/years, {month} month/months and {days_left} day/days.")