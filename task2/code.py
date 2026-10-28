# Case Study 26: Examination Seating

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

reserved_row = 1
reserved_col = 2

for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        if i == reserved_row and j == reserved_col:
            print("R", end="  ")
        else:
            print("S", end="  ")
    print()
