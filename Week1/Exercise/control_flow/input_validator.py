

def validate_password(password):
    """
    Write a function validate_password(password) that checks:

    At least 8 characters long
    Contains at least one uppercase letter
    Contains at least one lowercase letter
    Contains at least one digit
    Contains at least one special character (!@#$%^&*)
"""

    reasons_list=list()

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    is_valid=True

    special_chars = "!@#$%^&*"


    if len(password)<8:
        reasons_list.append(" too short")
    
    for character in password:

        if character.isupper():
            has_upper=True
        elif character.islower():
            has_lower=True
        elif character.isdigit():
            has_digit=True
        elif character in special_chars:
            has_special=True

    if not has_upper:
        is_valid=False
        reasons_list.append("no upper")
    if not has_lower:
        is_valid=False
        reasons_list.append("no lower")
    if not has_digit:
        is_valid=False
        reasons_list.append("no digit")
    if not has_special:
        is_valid=False
        reasons_list.append("no special")


    return {"valid":is_valid, "errors": reasons_list}

print(validate_password("Abc123!x"))    # valid
print(validate_password("abc"))         # too short, no upper, no digit, no special
print(validate_password("ABCDEFGH") )   # no lower, no digit, no special
print(validate_password("ABCDefgh1!"))  # valid
    


        



