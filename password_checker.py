import re

def check_password_strength(password):
    # Rules
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Evaluate
    errors = {
        "Too short (min 8 chars)": length_error,
        "Missing a digit": digit_error,
        "Missing an uppercase letter": uppercase_error,
        "Missing a lowercase letter": lowercase_error,
        "Missing a special symbol": symbol_error,
    }

    # Output result
    if not any(errors.values()):
        print("✅ Strong password!")
    else:
        print("❌ Weak password. Issues:")
        for issue, is_problem in errors.items():
            if is_problem:
                print(f"  - {issue}")

if __name__ == "__main__":
    user_password = input("Enter your password: ")
    check_password_strength(user_password)
