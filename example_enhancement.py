# Optional enhancement example (not recommended to change your current working code)

from string import ascii_lowercase
from typing import Set

from typing import Optional

def check_password(password: str, allowed_special: Optional[Set[str]] = None) -> bool:
    """
    Check if password meets requirements.
    
    Args:
        password: The password to check
        allowed_special: Set of allowed special characters (defaults to safe set)
    
    Returns:
        bool: True if password is valid, False otherwise
    """
    if allowed_special is None:
        allowed_special = {"$", "@", "#", "&", "!", "-", "_"}
    
    if len(password) not in range(8, 17):
        return False
        
    has_upper = False
    has_digit = False
    has_special = False
    
    for letter in password:
        if letter.isalpha():
            if letter.upper() == letter:
                has_upper = True
            if letter.lower() not in ascii_lowercase:
                return False
        elif letter.isdigit():
            has_digit = True
        elif letter in allowed_special:
            has_special = True
        else:
            return False
            
    return all([has_upper, has_digit, has_special])
