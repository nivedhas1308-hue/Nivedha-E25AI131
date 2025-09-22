def check_password_strength(password):
    strength = 0
    remarks = ""

    if len(password) < 6:
        remarks = "Too short! Use at least 6 characters."
        return "Weak", remarks
    elif len(password) >= 8:
        strength += 1

    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~" for c in password):
        strength += 1

    if strength <= 2:
        remarks = "Weak password. Add more character variety."
        return "Weak", remarks
    elif strength == 3 or strength == 4:
        remarks = "Moderate strength. Try adding symbols/length."
        return "Medium", remarks
    else:
        remarks = "Strong password!"
        return "Strong", remarks


password = input("Enter a password: ")
level, message = check_password_strength(password)
print("Password strength:", level)
print("Feedback:", message)
