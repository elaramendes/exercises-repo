import math

x_1 = int(input("Write the first pair, X: "))
y_1 = int(input("Write the first pair, Y: "))

x_2 = int(input("Write the second pair, X: "))
y_2 = int(input("Write the second pair, Y: "))

calc = ((x_2 - x_1)**2) + ((y_2 - y_1)**2)
result = math.sqrt(calc)

print(f'{result:.2f}')