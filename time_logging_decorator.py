import time
from string import ascii_letters, digits


def time_logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.8f} seconds to complete")
        return result

    return wrapper


@time_logger
def is_valid_original(password):
    if len(password) > 7:
        data_set = set(ascii_letters + digits + '_')
        if all(elem in data_set for elem in password):
            if all([any(elem.isupper() for elem in password), any(elem.islower() for elem in password),
                    any(elem.isdigit() for elem in password)]):
                return "+"
    return "-"


@time_logger
def is_valid_improved(password):
    if len(password) <= 7:
        return "-"

    allowed_chars = set(ascii_letters + digits + '_')

    has_upper = has_lower = has_digit = False

    for char in password:
        if char not in allowed_chars:
            return "-"
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    if has_upper and has_lower and has_digit:
        return "+"
    else:
        return "-"


if __name__ == "__main__":
    s = input("Enter the password: ")

    print("Original Function Result:", is_valid_original(s))
    print("Improved Function Result:", is_valid_improved(s))