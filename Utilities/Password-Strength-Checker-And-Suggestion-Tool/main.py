import getpass as gp
import string
import random

def check_availability(password):

    have_enough_length = len(password) >= 8
    have_lowercase = False
    have_uppercase = False
    have_digit = False
    have_special_char = False
    
    for char in password:
        if (not have_lowercase) and (char in string.ascii_lowercase):
            have_lowercase = True
        elif (not have_uppercase) and (char in string.ascii_uppercase):
            have_uppercase = True
        elif (not have_digit) and (char in string.digits):
            have_digit = True
        elif (not have_special_char) and (char in string.punctuation):
            have_special_char = True
        
    return have_enough_length, have_lowercase, have_uppercase, have_digit, have_special_char

def get_random_symbol_and_idx(password, symbol_seq):

    symbol = random.choice(symbol_seq)
    if not password:
        return symbol, 0
    return symbol, random.randint(0, len(password) - 1)

def gen_password(password, have_enough_length, have_lowercase, have_uppercase, have_digit, have_special_char):

    print("\nSuggestions: ")

    if not have_enough_length:
        print("- must be at least 8 characters long")
    
    if not have_lowercase:
        print("- must contain atleast one lowercase")
        random_lowercase, random_idx = get_random_symbol_and_idx(password, string.ascii_lowercase)
        password = password[:random_idx] + random_lowercase + password[random_idx:]
    
    if not have_uppercase:
        print("- must contain atleast one uppercase")
        random_uppercase, random_idx = get_random_symbol_and_idx(password, string.ascii_uppercase)
        password = password[:random_idx] + random_uppercase + password[random_idx:]
    
    if not have_digit:
        print("- must contain atleast one digit")
        random_digit, random_idx = get_random_symbol_and_idx(password, string.digits)
        password = password[:random_idx] + random_digit + password[random_idx:]
    
    if not have_special_char:
        print("- must contain atleast one special character")
        random_punctuation, random_idx = get_random_symbol_and_idx(password, string.punctuation)
        password = password[:random_idx] + random_punctuation + password[random_idx:]
    
    if (password_length := len(password)) < 8:
        for i in range(8 - password_length):
            random_type = random.choice([string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation])
            random_symbol, random_idx = get_random_symbol_and_idx(password, random_type)
            password = password[:random_idx] + random_symbol + password[random_idx:]

    return password


def check_password_strength(password):

    have_enough_length, have_lowercase, have_uppercase, have_digit, have_special_char = check_availability(password)

    if have_enough_length and have_lowercase and have_uppercase and have_digit and have_special_char:
        print("\nPassword is strong!")
        return True

    suggested_password = gen_password(password, have_enough_length, have_lowercase, have_uppercase, have_digit, have_special_char)

    print(f"\nHere is a strong password which you can use: {suggested_password}")

    return False


if __name__ == "__main__":


    while True:
        key = gp.getpass("Enter a password: ")
        if not key:
            print("Error: Please enter a non empty password\n")
            continue
        break

    check_password_strength(key)