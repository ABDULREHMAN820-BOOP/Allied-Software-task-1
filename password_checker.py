password = input("Enter your password: ")

has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(not char.isalnum() for char in password)

if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
    print("Password Status: Strong Password")
else:
    print("Password Status: Weak Password")
    print("Reason: Password must contain at least 8 characters, uppercase letter, lowercase letter, number, and special character.")