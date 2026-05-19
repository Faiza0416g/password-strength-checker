import re

def check_password_strength(password):
    strength_points = 0

    if len(password) >= 8:
        strength_points += 1

    if re.search(r"[A-Z]", password):
        strength_points += 1

    if re.search(r"[a-z]", password):
        strength_points += 1

    if re.search(r"\d", password):
        strength_points += 1

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength_points += 1

    if strength_points == 5:
        return "Very Strong Password ✅"
    elif strength_points >= 4:
        return "Strong Password 💪"
    elif strength_points >= 3:
        return "Medium Password ⚠️"
    else:
        return "Weak Password ❌"


password = input("Enter your password: ")

result = check_password_strength(password)

print("\nPassword Analysis Result:")
print(result)
