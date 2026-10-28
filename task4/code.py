# Case Study 28: Transaction Detection

transactions = [101, 102, 103, 102, 104, 101]

amounts = [500, 1200, 800, 1500, 300, 2000]

print("Duplicate Transactions:")

for i in range(len(transactions)):
    if transactions[i] in transactions[:i]:
        print(transactions[i])

print("Transactions above 1000:")

for i in range(len(amounts)):
    if amounts[i] > 1000:
        print(transactions[i], "-", amounts[i])

