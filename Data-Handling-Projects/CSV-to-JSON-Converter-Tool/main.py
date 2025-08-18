import os, csv, json

def load_csv(INPUT_FILE):
    try:
        with open(INPUT_FILE, 'r', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = list(reader)
            
            if not data:
                print("Error: CSV file is empty!")
                return False
        
            return data
    except FileNotFoundError:
        print(f"Error: No such file named '{INPUT_FILE}' exist!")
        return False


def save_to_json(data, OUTPUT_FILE):
    try:
        with open(OUTPUT_FILE, 'w', encoding="utf-8") as f:
            json.dump(data, f, indent=2)
            print(f"Converted {len(data)} {'record!' if len(data) == 1 else 'records!'}")
            return True
    except (OSError, TypeError) as e:
        print(f"Error: Couldn't save to JSON because -> '{e}'")
        return False


def preview_json(data, count=3):

    prompt = "--- Sample of converted JSON file ---"
    print(f"\n{prompt}")

    print(json.dumps(data[:min(len(data), count)], indent=2))

    print(f"{'more record(s)...\n' if len(data) > count else ''}", end='')
    
    print('-' * len(prompt))


def main():
    INPUT_FILE = "raw_data.csv"
    OUTPUT_FILE = "converted_data.json"

    data = load_csv(INPUT_FILE)

    if data is False:
        return
    
    if save_to_json(data, OUTPUT_FILE):
        print(f"Successfully converted: {INPUT_FILE} -> {OUTPUT_FILE}!")
        preview_json(data)
        return True
    else:
        print("Error: Something went wrong. Try again...")
        return False


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()