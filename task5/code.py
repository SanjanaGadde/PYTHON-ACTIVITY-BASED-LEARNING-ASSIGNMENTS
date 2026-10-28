# Case Study 29: Password Validation

password = input("Enter a password: ")

upper = False
lower = False
digit = False
special = False

for ch in password:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True
    else:
        special = True

if len(password) >= 8 and upper and lower and digit and special:
    print("Password is valid")
else:
    print("Password is invalid")

    if len(password) < 8:
        print("Password must contain 8 characters")
    if not upper:
        print("Add an uppercase letter")
    if not lower:
        print("Add a lowercase letter")
    if not digit:
        print("Add a digit")
    if not special:
        print("Add a special character")
