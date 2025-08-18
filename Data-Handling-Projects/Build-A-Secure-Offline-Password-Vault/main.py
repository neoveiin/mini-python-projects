import string
import base64
import os


VAULT_FILE = "vault.txt"


def vault_exists():
    if os.path.isfile(VAULT_FILE):
        return True
    return False


def decode_credential(encoded_credential):
    cred = base64.b64decode(encoded_credential.encode()).decode()
    return cred.split("||")


def encode_credential(website, username, password):
    cred = f"{website}||{username}||{password}"
    return base64.b64encode(cred.encode()).decode()


def load_credentials():

    if not vault_exists():
        return []
    
    with open(VAULT_FILE, 'r', encoding="utf-8") as f:
        encoded_credentials = f.read().splitlines()
        return encoded_credentials


def website_exists(website):
    if not vault_exists():
        return False
    
    credentials = load_credentials()

    for credential in credentials:
        stored_website, *_ = decode_credential(credential)

        if website.lower() == stored_website.lower():
            return True
    
    return False


def password_strength(password):

    length = len(password)
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    score = sum((length >= 8, has_lower, has_upper, has_digit, has_special))

    if score == 5:
        return "strong"
    elif score > 2:
        return "medium"
    else:
        return "weak"


def add_credential():
    print()

    website = input("Enter website: ").strip()

    if website_exists(website):
        print(f"Error: Credentials for entered website already exists! Try updating it...")
        return False

    while True:
        username = input("Enter username: ").strip()
        if not username:
            continue
        while True:
            password = input("Enter password: ").strip()
            if not password:
                continue
            break
        break

    with open(VAULT_FILE, 'a', encoding="utf-8") as f:
        f.write(encode_credential(website, username, password) + '\n')

    print(f"\nYour password is {password_strength(password)}!")

    print(f"Credentials for {website} saved successfully!")

    return True


def view_all_credentials():

    if not vault_exists():
        print("Error: No credentials exist to display. Try adding one...")
        return False

    print()

    credentials = load_credentials()

    for credential in credentials:
        website, username, password = decode_credential(credential)
        print(f"{website} | {username} | {password}")
    
    return True


def save_credentials(credentials):

    with open(VAULT_FILE, 'w', encoding="utf-8") as f:
        for credential in credentials:
            f.write(credential+'\n')


def update_credential():

    if not vault_exists():
        print("Error: No credentials exist to update. Try adding one...")
        return False

    print()

    website = input("Enter website to update its credentials: ").strip()

    if not website_exists(website):
        print(f"Error: No such website exists. Try adding one...")
        return False
    
    while True:
        new_username = input("Enter new username: ").strip()
        if not new_username:
            continue
        while True:
            new_password = input("Enter new password: ").strip()
            if not new_password:
                continue
            break
        break

    credentials = load_credentials()

    updated_credentials = []

    for credential in credentials:
        stored_website, *_ = decode_credential(credential)
        if website.lower() == stored_website.lower():
            updated_credentials.append(encode_credential(website, new_username, new_password))
        else:
            updated_credentials.append(credential)

    save_credentials(updated_credentials)

    print(f"\nSuccessfully updated credentials for website '{website}'")


def search_credential():

    if not vault_exists():
        print("Error: No credentials exist to search. Try adding one...")
        return False

    print()

    website = input("Enter website to search: ").strip()

    if not website_exists(website):
        print(f"Error: No such website exists!")
        return False

    credentials = load_credentials()

    cred_found = False

    for credential in credentials:
        stored_website, username, password = decode_credential(credential)
        if website.lower() == stored_website.lower():
            print(f"{stored_website} | {username} | {password}")
            cred_found = True
    
    if not cred_found:
        print("\nNo matching records found!")
    
    return True


def main():
    
    while True:

        menu = "--- Offline Password Manager ---\n"
        border_len = len(menu)
        menu += "1. Add credential\n"
        menu += "2. View all credentials\n"
        menu += "3. Update credentials\n"
        menu += "4. Search credentials\n"
        menu += "5. Exit"
        print(menu)
        print('-' * border_len)
        choice = input("Enter your choice: ").strip()

        match choice:
            case "1":
                add_credential()
            case "2":
                view_all_credentials()
            case "3":
                update_credential()
            case "4":
                search_credential()
            case "5":
                print("\nThanks for using the software!")
                break
            case _:
                print(f"Error: Enter a valid choice (1-5). Provided: '{choice}'")
        
        print()
        

if __name__ == "__main__":
    main()
