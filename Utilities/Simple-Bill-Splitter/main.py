def get_int(prompt):
    while True:
        try:
            val = int(input(prompt))
            return val
        except:
            print("X: enter an integer value only!")

def get_float(prompt):
    while True:
        try:
            val = float(input(prompt))
            return val
        except:
            print("X: enter a floating point value only!")

def get_float(prompt):
    while True:
        user = input(prompt)

        if user.isdigit():
            return int(user)
        else:
            print("X: enter an integer value only")


def bill_splitter():
    count = get_int("How many people are there in the group? ")

    group = []

    print()

    for i in range(1, count+1):
        name = input(f"Enter name of person {i}: ").strip()
        group.append(name)
    
    print()

    total_amount = get_float("Enter total bill amount: ")

    per_head = round(total_amount / count, 2)

    print(f"\nSummary:")

    for person in group:
        print(f"{person} owes INR {per_head}")
    
if __name__ == "__main__":
    bill_splitter()
