from datetime import datetime

def calculate_check_digit (nine_digits: str) -> str:
    """Takes a 9 character digit string, and it returns the check digit as a string"""
    if len(nine_digits) != 9 or not nine_digits.isdigit():
        raise ValueError("Input must be exactly 9 digits")

    total = 0
    for position, char in enumerate(nine_digits, start=1):
        digit = int(char)
        total += digit * position

    check_digit = total % 10
    return str(check_digit)

def generate_full_id(nine_digits: str) -> str:
    """Builds a brand new 10-digit ID with the chack digit appended"""
    check = calculate_check_digit(nine_digits)
    return nine_digits + check

def validate_id(full_id: str) -> bool:
    """Validates a 10-digit ID by recomputing its check digit"""
    if len(full_id) != 10 or not full_id.isdigit():
        return False

    nine_digits = full_id[:9]
    provided_check = full_id[9]
    expected_check = calculate_check_digit(nine_digits)

    return provided_check == expected_check

def is_valid_date(date_str: str) -> bool:
    """Validates a date string which is in yyyy-mm-dd format and is a real calendar date"""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    test_id = generate_full_id('314159265')
    print(f"Generated ID: {test_id}")
    print(f"Validates as True: {validate_id(test_id)}")
    print(f"Validates as False: {validate_id('3141592658')}")

    print(f"Valid date: {is_valid_date('2026-07-12')}")
    print(f"Invalid date: {is_valid_date('2026-20-30')}")
