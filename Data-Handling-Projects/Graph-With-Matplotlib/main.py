import csv
from collections import defaultdict as dd
from matplotlib import pyplot as plt
import os

FILENAME = "weather_logs.csv"

def visualize_weather_logs():
    try:
        with open(FILENAME, 'r', encoding='utf-8') as f:
            logs = csv.DictReader(f)

            try:
                if not dict(logs):
                    print("Error: No logs available to visualize!")
                    return
            except ValueError:
                pass

            dates, temps = [], []
            conditions = dd(int)

            for row in logs:
                dates.append(row["Date"])
                temps.append(row["Temperature"])
                conditions[row["Condition"]] += 1

    except FileNotFoundError:
        print(f"Error: No such file named '{FILENAME}' exists!")
        return
    
    # Plotting Graph 1: Date Vs Temp for Delhi
    plt.figure(figsize=(12, 7))
    plt.title("Date Vs Temperature (°C) (Delhi)")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.tight_layout()
    plt.plot(dates, temps, marker='o')
    plt.show()

    # Plotting Graph 2: Frequency of Weather Conditions in Delhi
    plt.figure(figsize=(10, 5))
    plt.title("Frequency of Weather Conditions in Delhi")
    plt.xlabel("Weather Condition")
    plt.ylabel("Occurrence(s)")
    plt.grid(True)
    plt.tight_layout()
    plt.plot(conditions.keys(), conditions.values(), marker='o')
    plt.show()
    
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')

    visualize_weather_logs()