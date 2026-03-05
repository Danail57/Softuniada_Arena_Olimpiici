def password_has_small_letter(password: str):
    for symbol in password:
        if symbol.islower():
            return True
    return False

def password_has_upper_letter(password: str):
    for symbol in password:
        if symbol.isupper():
            return True
    return False

def password_has_digit(password: str):
    for symbol in password:
        if symbol.isdigit():
            return True
    return False

def password_has_no_consecutive_same_symbols(password: str):
    has_consecutive_same_symbols = False
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            return False
    return True


password = input()
if (len(password) == 6 and
        password_has_small_letter(password) and
        password_has_upper_letter(password) and
        password_has_digit(password) and
        password_has_no_consecutive_same_symbols(password)):
    print("YES")
else:
    print("NO")
