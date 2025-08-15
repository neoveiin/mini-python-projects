def error(err):
    RED = '\033[31m'
    RESET = '\033[0m'

    print(f"{RED}error: {err}{RESET}\n")

def alive(age):
    DAYS_IN_A_YEAR = 365.25
    HOURS_IN_A_DAY = 24
    MINUTES_IN_AN_HOUR = 60

    days_alive = age * DAYS_IN_A_YEAR
    hours_alive = days_alive * HOURS_IN_A_DAY
    minutes_alive = hours_alive * MINUTES_IN_AN_HOUR

    return round(days_alive, 2), round(hours_alive, 2), round(minutes_alive, 2)

while True:

    try:
        age = float(input("Enter your age in years? (float value accepted) "))
    except:
        error("enter a valid age")
        continue

    days, hours, minutes = alive(age)

    print("\nYou're approximately:")

    print(f"  - {days} days old")
    print(f"  - {hours} hours old")
    print(f"  - {minutes} minutes old")

    do_repeat = input("\nDo you want to try again (y/n): ").strip().lower()

    if do_repeat != 'y':
        print("\nGood Bye!")
        break

    print()