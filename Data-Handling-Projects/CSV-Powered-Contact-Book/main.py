import csv
import os
import sys

FILENAME = "contacts.csv"

def error(err, newline=False):
    RED = '\033[31m'
    RESET = '\033[0m'
    print(f"{RED}Error: {err}{RESET}{'\n' if newline else ''}")
    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def hold():
    input("\nPress Enter to continue...")

def database_validation(filename):

    if not os.path.isfile(filename):
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            wo = csv.writer(f, delimiter=':')
            wo.writerow(["name", "phone", "email"])
            return
    else:
        with open(filename, 'r', encoding='utf-8') as f:
            ro = csv.reader(f, delimiter=':')
            if next(ro) == ["name", "phone", "email"]:
                return
            
    overwrite = input("There already exists a corrupted database.\n"
                        "Would you like to overwrite it (y/n)? "
                ).strip().lower()

    if overwrite == 'y':
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            wo = csv.writer(f, delimiter=':')
            wo.writerow(["name", "phone", "email"])
            return
    else:
        print("\nThanks for using the Contact Manager. Have a nice day!")
        sys.exit()

def get_str(prompt):

    while True:
        val = input(prompt).strip()

        if not val:
            error("Enter a valid string literal")
            continue

        return val

def is_empty():
    with open(FILENAME, 'r', encoding='utf-8') as f:
        ro = csv.reader(f, delimiter=':')
        next(ro)

        rows = list(ro)
        
        if len(rows) == 0:
            return True
        return False

def already_exists(phone):
    if is_empty():
        return False
    
    with open(FILENAME, 'r', encoding='utf-8') as f:
        ro = csv.reader(f, delimiter=':')

        next(ro)

        rows = list(ro)

        for row in rows:
            if phone.strip() == row[1]:
                return True
        
        return False

def add_contact():
    clear_screen()
    
    name = get_str("\nName: ")
    phone = get_str("\nPhone: ")
    email = get_str("\nEmail: ")

    if already_exists(phone):
        print("\nContact with similar phone already exists! Try again.")
        hold()
        return

    with open(FILENAME, 'a', newline='', encoding='utf-8') as f:
            wo = csv.writer(f, delimiter=':')
            wo.writerow([name, phone, email])
    
    print("\nContact created successfully!\n")

    hold()

def print_table(rows):

    name_max = max(len(row[0]) for row in rows)
    phone_max = max(len(row[1]) for row in rows)
    email_max = max(len(row[2]) for row in rows)

    border = "**" + ("*" * name_max) + "***" + ("*" * phone_max) + "***" + ("*" * email_max) + "**"

    print(border)

    print("| ", end='')
    print("name", end='')
    for i in range(name_max - len("name")):
        print(' ', end='')
    print(" | ", end='')
    print("phone", end='')
    for i in range(phone_max - len("phone")):
        print(' ', end='')
    print(" | ", end='')
    print("email", end='')
    for _ in range(email_max - len("email")):
        print(' ', end='')
    print(" |")
    
    print(border)

    for row in rows:
        print("| ", end='')
        print(row[0], end='')
        for i in range(name_max - len(row[0])):
            print(' ', end='')
        print(" | ", end='')
        print(row[1], end='')
        for i in range(phone_max - len(row[1])):
            print(' ', end='')
        print(" | ", end='')
        print(row[2], end='')
        for _ in range(email_max - len(row[2])):
            print(' ', end='')
        print(" |")

    print(border)

def view_contacts():
    clear_screen()

    if is_empty():
        print("\nContact list is empty!")
        hold()
        return

    with open(FILENAME, 'r', encoding='utf-8') as f:
        ro = csv.reader(f, delimiter=':')
        next(ro)

        rows = list(ro)

        print_table(rows)
    
    hold()

def search_contact():
    clear_screen()

    if is_empty():
        print("\nContact list is empty!")
        hold()
        return

    string = get_str("Enter a string to search: ").strip().lower()

    with open(FILENAME, 'r', encoding='utf-8') as f:
        ro = csv.reader(f, delimiter=':')
        next(ro)

        rows = list(ro)

        results = []

        for row in rows:
            if string in row[0]:
                results.append(row)
        
        if not results:
            print("\nNo such contact found!")
            hold()
            return
    
        print("\nSearch Result: ")

        print_table(results)
    
    hold()

def update_contact():
    clear_screen()

    if is_empty():
        print("\nContact list is empty!")
        hold()
        return
    
    phone = get_str("Enter phone number to update that enty: ")

    if not already_exists(phone):
        print("\nNo such contact exists! Try again.")
        hold()
        return
    
    print("\nThere exists a contact with this phone number!\n")

    new_name = input("Enter new name (Press Enter to keep it intact): ")
    new_phone = input("Enter new phone (Press Enter to keep it intact): ")
    new_email = input("Enter new email (Press Enter to keep it intact): ")

    if already_exists(new_phone):
        print("\nContact with similar phone already exists! Try again.")
        hold()
        return

    if not new_name and not new_phone and not new_email:
        print("\nNo, updation occcured as no changes were mentioned. Try again.")
        hold()
        return

    with open(FILENAME, 'r', encoding='utf-8') as f:
        ro = csv.reader(f, delimiter=':')
        next(ro)

        rows = list(ro)

        for row in rows:
            if phone == row[1]:
                if new_name:
                    row[0] = new_name
                if new_phone:
                    row[1] = new_phone
                if new_email:
                    row[2] = new_email
                break
                
    
    with open(FILENAME, 'w', newline='', encoding='utf-8') as f:
        wo = csv.writer(f, delimiter=':')
        wo.writerow(["name", "phone", "email"])
        wo.writerows(rows)
    
    print("\nContact updated successfully!")
    hold()
    return

def delete_contact():
    clear_screen()

    if is_empty():
        print("\nContact list is empty!")
        hold()
        return
    
    phone = get_str("Enter phone number to delete that enty: ")

    if not already_exists(phone):
        print("\nNo such contact exists! Try again.")
        hold()
        return
    
    with open(FILENAME, 'r', encoding='utf-8') as f:
        ro = csv.reader(f, delimiter=':')
        next(ro)

        rows = list(ro)

        for idx, row in enumerate(rows):
            if phone == row[1]:
                del_name, del_phone, del_email = row
                print(
                    "\nBelow details got deleted successfully:\n"
                    f"Name: {del_name}\n"
                    f"Phone: {del_phone}\n"
                    f"Email: {del_email}\n"
                )
                rows.pop(idx)
                break
    
    with open(FILENAME, 'w', newline='', encoding='utf-8') as f:
        wo = csv.writer(f, delimiter=':')
        wo.writerow(["name", "phone", "email"])
        wo.writerows(rows)
    
    hold()
    return


def main():

    database_validation(FILENAME)

    while True:

        clear_screen()

        print("--- Contacts Manager ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
    
        choice  = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("\nThanks for using the Contact Manager. Have a nice day!")
            break
        else:
            error(f"Error: Enter a valid choice between 1 and 6. Provided: '{choice}'")
            hold()

if __name__ == "__main__":
    main()
