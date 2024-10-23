small_shirts = int(input("How many small shirts did you sell? "))
medium_shirts = int(input("How many medium shirts did you sell? "))
big_shirts = int(input("How many big shirts did you sell? "))

total = (small_shirts * 10) + (medium_shirts * 12) + (big_shirts * 15)

print(f"The total will be R$ {total}")