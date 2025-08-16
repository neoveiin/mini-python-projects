import os

def error(err, newline=False):
    RED = '\033[31m'
    RESET = '\033[0m'
    print(f"{RED}Error: {err}{RESET}{'\n' if newline else ''}")

def encrypt(message, key):
    encrypted_msg = ""

    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_ascii_val = ((ord(char) - base + key) % 26) + base
            encrypted_msg += chr(new_ascii_val)
        else:
            encrypted_msg += char
    
    return encrypted_msg

def decrypt(message, key):
    return encrypt(message, -key)

def caesar_cipher():

    while True:
        choice = input("Would you like to (e)ncrypt or (d)ecrypt a message: ").strip().lower()
        
        if choice not in {'e', 'd'}:
            error(f"Enter, 'e' for Encrypting or 'd' for Decrypting a message. Provided: '{choice}'", True)
            continue

        break

    print()

    while True:
        msg = input("Enter your secret message: ")

        if not msg:
            error("Enter a non empty message", True)
            continue

        break

    print()

    while True:
        try:
            key = int(input("Enter secret key: "))
            if key == 0:
                error("Value of secret key can't be zero", True)
                continue
            break
        except ValueError:
            error(f"Enter a valid integer value", True)
            continue
    
    print()

    match choice:
        case 'e':
            print(f"Your encrypted message: {encrypt(msg, key)}")
        case 'd':
            print(f"Your decrypted message: {decrypt(msg, key)}")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')

    print("--- Welcome to the Caesar Cipher ---\n")

    caesar_cipher()