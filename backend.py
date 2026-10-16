def password_strength(password):
    score = 0
    has_uppercase = False
    has_digit = False
    has_special = False

    special_characters = '!@#$%^&*(),.?":{}|<>'

    for character in password:
        if character.isupper():
            has_uppercase = True
        if character.isdigit():
            has_digit = True
        if character in special_characters:
            has_special = True

    if len(password) >= 12:
        score += 3
    elif len(password) >= 8:
        score += 1

    if has_uppercase:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    if score >= 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    elif score >= 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Max score is now 6 instead of 7
    percentage = int((score / 6) * 100)

    return {
        "score": score,
        "percentage": percentage,
        "strength": strength,
        "details": {
            "length_8": len(password) >= 8,
            "length_12": len(password) >= 12,
            "uppercase": has_uppercase,
            "digit": has_digit,
            "special": has_special
        }
    }