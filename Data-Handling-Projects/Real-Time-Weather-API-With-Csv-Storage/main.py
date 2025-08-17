import os
import csv
from datetime import datetime
import requests
import sys

# global variable(s)
FILENAME = "weather_log.csv"
API_KEY = "b0a1c8bdbb9e20a16016709538edf8e3" # API keys are usually hidden in .env file (but that I'll learn later)
HEADERS = ["Date", "City", "Temperature", "Condition"]

def setup():
    if not os.path.isfile(FILENAME):
        with open(FILENAME, 'w', newline='', encoding='utf-8') as f:
            wo = csv.writer(f)
            wo.writerow(HEADERS)
            return
    with open(FILENAME, 'r', encoding='utf-8') as f:
        ro = csv.reader(f)
        if next(ro) != HEADERS:
            overwrite = input(
                "There already exists a corrupted log file.\n"
                "Would you like to overwrite it and start fresh (y/n)? "
            ).strip()

            if overwrite.lower() == 'y':
                with open(FILENAME, 'w', newline='', encoding='utf-8') as f:
                    wo = csv.writer(f)
                    wo.writerow(HEADERS)
                    print()
                    return
            
            print("Operation cancelled. Thanks for using Weather Logger!")
            sys.exit()


def city_already_exists(city_name, date):
    with open(FILENAME, 'r', encoding='utf-8') as f:
        ro = csv.reader(f)
        next(ro)

        rows = list(ro)

        if not rows:
            return False
        
        for row in rows:
            if date == row[0] and city_name.lower() == row[1].lower():
                return True
        
        return False
        

def add_entry(date, city_name, temperature, condition):
    with open(FILENAME, 'a', newline='', encoding='utf-8') as f:
        wo = csv.writer(f)
        wo.writerow([date, city_name, temperature, condition])


def add_weather_log():
    print()

    current_date = datetime.now().strftime("%d/%m/%Y")
    city_name = input("Enter city name: ").strip()
    
    if not city_name:
        print("\nError: Enter a non empty city name")
        return
    
    if city_already_exists(city_name, current_date):
        print(f"\nError: Entry for city '{city_name}' already exists for today. Try viewing it...")
        return

    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name.lower()}&appid={API_KEY}&units=metric"

        response = requests.get(url)

        if response.status_code != 200:
            print("\nError: API call failed. Try again...")
            return
        
        data = response.json()

    except:
        print("\nError: API call failed. Try again...")
        return
    
    else:
        temperature = data["main"]["temp"]
        condition = data["weather"][0]["main"]

        add_entry(current_date, city_name, temperature, condition)

        print(f"\nLogged weather information for '{city_name}' city on '{current_date}'")


def draw_weather_table(data):
    # Define headers
    headers = ["Date", "City", "Temperature (°C)", "Condition"]
    
    # Find the max width of each column
    col_widths = [len(h) for h in headers]
    for row in data:
        for i, value in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(value)))
    
    # Helper function to format each row
    def format_row(row):
        return " | ".join(
            (str(val).title() if i == 1 else str(val)).ljust(col_widths[i]) 
            for i, val in enumerate(row)
        )
    
    # Draw the header
    table = format_row(headers)
    table += "\n" + "-+-".join("-" * w for w in col_widths)
    
    # Draw rows
    for row in data:
        table += "\n" + format_row(row)
    
    return table


def view_all_weather_logs():
    print()

    with open(FILENAME, 'r', encoding='utf-8') as f:
        ro = csv.reader(f)
        next(ro)

        rows = list(ro)

        if not rows:
            print("\nNo weather information has been logged yet. Try adding one to view them...")
            return
        
        print(draw_weather_table(rows))


def show_stats():
    print()

    with open(FILENAME, 'r', encoding='utf-8') as f:
        ro = csv.reader(f)
        next(ro)

        rows = list(ro)

        all_temps = [
            float(row[2])
            for row in rows
        ]

        avg_temp = round(sum(all_temps) / len(all_temps), 2)
        max_temp = max(all_temps)
        min_temp = min(all_temps)

        cities_with_max_temp = [
            row[1]
            for row in rows
            if float(row[2]) == max_temp
        ]

        cities_with_min_temp = [
            row[1]
            for row in rows
            if float(row[2]) == min_temp
        ]

        freq_of_conditions = {}

        for row in rows:
            if row[3] not in freq_of_conditions:
                freq_of_conditions[row[3]] = 1
            else:
                freq_of_conditions[row[3]] += 1
        
        most_freq_conditions = [
            condition
            for condition in freq_of_conditions
            if freq_of_conditions[condition] == max(freq_of_conditions.values())
        ]
    
    stats = "---- Weather Stats (All Time) ----"
    temp = len(stats)
    stats += f"\n- Average temp: {avg_temp}°C"
    stats += f"\n- Max temp: {max_temp}°C in {', '.join(city_name.title() for city_name in cities_with_max_temp)}"
    stats += f"\n- Min temp: {min_temp}°C in {', '.join(city_name.title() for city_name in cities_with_min_temp)}"
    stats += f"\n- Most frequent conditions: {', '.join(most_freq_conditions)}"
    stats += f"\n{'-' * temp}"

    print(stats)


def weather_logger_app():

    os.system('cls' if os.name == 'nt' else 'clear')

    setup()

    while True:

        menu = "--- Weather Logger ---"
        menu += "\n1. Add new weather log"
        menu += "\n2. View all logs"
        menu += "\n3. Show statistics"
        menu += "\n4. Exit"

        print(menu)

        choice = input(f"Enter choice (1-3): ").strip()

        match choice:
            case '1': add_weather_log()
            case '2': view_all_weather_logs()
            case '3': show_stats()
            case '4':
                print("\nThanks for using weather logger!")
                break
            case _:
                print(f"\nError: Enter valid choice between 1 and 3. Provided: '{choice}'\n")
                continue
        
        print()


if __name__ == "__main__":
    weather_logger_app()