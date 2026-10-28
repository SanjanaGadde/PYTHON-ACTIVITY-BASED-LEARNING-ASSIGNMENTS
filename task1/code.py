
# Case Study 25: Water Tariff Analysis

n = int(input("Enter water consumption in litres: "))

fixed_fee = 50

if n <= 1000:
    bill = n * 0.02
elif n <= 2000:
    bill = 1000 * 0.02 + (n - 1000) * 0.04
else:
    bill = 1000 * 0.02 + 1000 * 0.04 + (n - 2000) * 0.06

if n > 3000:
    penalty = 100
else:
    penalty = 0

total = bill + fixed_fee + penalty

print("Water Consumption:", n, "litres")
print("Water Bill:", bill)
print("Fixed Fee:", fixed_fee)
print("Penalty:", penalty)
print("Total Bill:", total)
