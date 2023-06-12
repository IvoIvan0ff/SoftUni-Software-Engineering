def password_validation(password):
    is_password_valid = True
    if not 6 <= len(password) <= 10:
        is_password_valid = False
        print("Password must be between 6 and 10 characters")

    if not password.isalnum():
        is_password_valid = False
        print("Password must consist only of letters and digits")

    digit_counter = 0
    for char in password:
        if char.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        is_password_valid = False
        print("Password must have at least 2 digits")

    if is_password_valid:
        print("Password is valid")


current_password = input()
password_validation(current_password)
