#Case Study 30:Student Email and Identifier Validation

email = input("Enter student email: ")
reg_no = input("Enter registration number: ")

if "@" in email and "." in email and email.index("@") < email.rindex("."):
    print("Email is valid")
else:
    print("Email is invalid")

if len(reg_no) == 10 and reg_no.isalnum():
    print("Registration number is valid")
else:
    print("Registration number is invalid")
