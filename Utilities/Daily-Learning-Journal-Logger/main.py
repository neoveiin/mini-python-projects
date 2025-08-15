from datetime import datetime as dt

def error(err, newline=False):
    RED = '\033[31m'
    RESET = '\033[0m'

    print(f"{RED}error: {err}{RESET}{'\n' if newline else ''}")

def daily_journal():
    learning = input("What special you learned today: ")
    
    while True:
        try:
            rating = input("Rate your day (1-5) [optional]: ")
            if not rating:
                break
            rating = int(rating)
        except:
            error("enter a valid integer value")
            continue
        if not (1 <= rating <= 5):
            error("enter a value between 1 and 5")
            continue
        break

    timestamp = dt.now()
    timestamp = timestamp.strftime("%Y/%b/%d (%a) - %I:%M:%S %p")

    entry = (
        f"📅 {timestamp}\n"
        f"🧠 Learning: {learning}\n"
        f"{f'🚀 Productivity Rating: {rating}/5\n' if rating else ''}"
        f"{'-*' * 25}\n"
    )

    filename = "learning_journal.txt"

    with open(filename, 'a', encoding="utf-8") as f:
        f.write(entry)
    
    print("Your entry has been successfully logged!")

daily_journal()