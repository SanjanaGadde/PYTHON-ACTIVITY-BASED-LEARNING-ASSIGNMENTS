# Case Study 32: Invoice Data Extraction

invoices = [
    "P101,2,500",
    "P102,3,900",
    "P103,1,250",
    "P104,abc,400"
]

for invoice in invoices:
    data = invoice.split(",")

    if len(data) == 3:
        code = data[0]
        quantity = data[1]
        amount = data[2]

        if quantity.isdigit() and amount.isdigit():
            print("\nProduct Code:", code)
            print("Quantity:", quantity)
            print("Amount:", amount)
        else:
            print("\nInvalid invoice:", invoice)
    else:
        print("\nInvalid invoice:", invoice)
