import string
import os

COMMON_PASSWORDS_PATH = os.path.join(os.path.dirname(__file__), "common_passwords.txt")

def load_common_passwords():
    try:
        with open(COMMON_PASSWORDS_PATH, "r") as file:
            return set(p.strip().lower() for p in file.readlines())
    except FileNotFoundError:
        return set()

COMMON_PASSWORDS = load_common_passwords()

def check_password_strength(password: str) -> dict:
    score = 0
    suggestions = []
    password_lower = password.lower()

    if password_lower in COMMON_PASSWORDS:
        return {
            "password": password,
            "strength": "Very Weak",
            "score": 0,
            "suggestions": ["Avoid common passwords."]
        }

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if any(c.islower() for c in password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        suggestions.append("Add special characters (e.g., @, #, $, !).")

    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return {
        "password": password,
        "strength": strength,
        "score": score,
        "suggestions": suggestions
    }

if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    result = check_password_strength(password)
    print(f"\nStrength: {result['strength']}")
    print("Suggestions:")
    for suggestion in result["suggestions"]:
        print(f" - {suggestion}")
