import sys
import json
import os
from cryptography.fernet import Fernet
from datetime import datetime
import base64
import time

VAULT_FILE = "notes.vault"
KEY_FILE = "vault.key"
AUTH_FILE = "master.key"

def fetch_key():
    if os.path.isfile(KEY_FILE):
        with open(KEY_FILE, "rb") as f:
            key = f.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
    
    return Fernet(key)

FERNET = fetch_key()

def do_vault_exist():
    if os.path.isfile(VAULT_FILE):
        return True
    return False

def load_vault():

    if do_vault_exist():
        with open(VAULT_FILE, 'r', encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    
    with open(VAULT_FILE, 'w', encoding="utf-8") as f:
        json.dump([], f)
        return []

def save_vault(notes):

    with open(VAULT_FILE, 'w', encoding="utf-8") as f:
        json.dump(notes, f, indent=2)
        return

def encrypt_content(content):
    return FERNET.encrypt(content.encode()).decode()

def decrypt_content(content):
    return FERNET.decrypt(content.encode()).decode()

def add_note():
    print()

    while True:
        title = input("Enter note title: ").strip()
        if not title:
            print("Error: Enter a non empty title!")
            continue
        break
        
    while True:
        content = input("Enter note content: ").strip()
        if not content:
            print("Error: Enter a non empty title!")
            continue
        break

    timestamp = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")

    notes = load_vault()

    notes.append({
        "title": title,
        "content": encrypt_content(content),
        "timestamp": timestamp
    })

    save_vault(notes)

    print("\nNote created successfully!")

def list_notes():
    print()

    notes = load_vault()

    if not notes:
        print("No notes to display!")
        return False

    print("--- All Notes ---")
    for sr_no, note in enumerate(notes, 1):
        print(f"{sr_no}. {note['title']} - {note['timestamp']}")

def view_note():
    
    if list_notes() is False:
        return
    
    print('-' * 17)

    notes = load_vault()
    while True:
        try:
            sr_no = int(input(f"Enter your choice ({1 if len(notes)==1 else f'1-{len(notes)}'}): "))
            
            if not (1 <= sr_no <= len(notes)):
                print(f"Error: Enter choice in this range only ({1 if len(notes)==1 else f'1-{len(notes)}'})")
                continue

            break

        except ValueError:
            print("Error: Enter a valid integer value!")
            continue
    
    idx = sr_no - 1

    decrypted_content = decrypt_content(notes[idx]["content"])

    title = f"Title: {notes[idx]["title"]}"
    timestamp = f"Timestamp: {notes[idx]["timestamp"]}"
    content = f"Content: {decrypted_content}"

    border_len = max(len(title), len(timestamp))

    print("\nHere's your Secret Note:")
    print('-' * border_len)
    print(title)
    print(timestamp)
    print(content)
    print('-' * border_len)

def search_notes():
    print()

    notes = load_vault()

    if not notes:
        print("No notes to search!")
        return
    
    while True:
        keyword = input("Enter a keyword: ").strip().lower()

        if not keyword:
            print("Error: Enter a non empty keyword!")
            continue

        break

    search_result = []

    for note in notes:
        if keyword in note["title"].lower():
            search_result.append(note)
    
    if not search_result:
        print("Oops! No search result.")
        return
    
    print("\n--- Search Results ---")
    for sr_no, note in enumerate(search_result, 1):
        print(f"{sr_no}. {note['title']} - {note['timestamp']}")

def authentication():
    if not os.path.isfile(AUTH_FILE):
        while True:
            master_key = input("Create a master key: ").strip()

            if not master_key:
                print("Error: Create a non-empty master key!")
                continue
            break
        
        with open(AUTH_FILE, 'w', encoding="utf-8") as f:
            encrypted_key = base64.b64encode(master_key.encode()).decode()
            f.write(encrypted_key)

        print("\nMaster key creation successfull!")

        for _ in range(3, 0, -1):
            print('. ', end='', flush=True)
            time.sleep(1)
        
        os.system('cls' if os.name == 'nt' else 'clear')

        authentication()
    else:

        print("Login Page:")

        with open(AUTH_FILE, 'r', encoding="utf-8") as f:
            master_key = f.read()
            decrypted_key = base64.b64decode(master_key.encode()).decode()

        for i in range(1, 4):
            user_key = input(f"Attempt-#{i}: Enter master key: ").strip()

            if user_key == decrypted_key:
                print("\nAccess Granted!")

                for _ in range(3, 0, -1):
                    print('. ', end='', flush=True)
                    time.sleep(1)
                
                os.system('cls' if os.name == 'nt' else 'clear')
                return

        print("\nAttempts exhausted! Try again...")
        sys.exit(1)

def main():

    authentication()

    while True:

        menu = "--- Offline Secure Notes ---\n"
        border_len = len(menu)
        menu += "1. Add note\n"
        menu += "2. List notes\n"
        menu += "3. View note\n"
        menu += "4. Search notes\n"
        menu += "5. Exit"
        print(menu)
        print('-' * border_len)
        choice = input("Enter your choice (1-5): ").strip()

        match choice:
            case '1': add_note()
            case '2': list_notes()
            case '3': view_note()
            case '4': search_notes()
            case '5': print("\nThanks for using 'Offline Secure Notes'"); break
            case _: print("Error: Enter a valid choice!")
        
        print()

if __name__ == "__main__":
    main()