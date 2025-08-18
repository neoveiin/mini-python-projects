import os, json, sys

INPUT_FILE = "nested_data.json"
OUTPUT_FILE = "flattened_data.json"

def load_json(filename):
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print(f"Error: Can't load '{filename}', b'coz it seems to be corrupted!")
                return False
            
            return data

    except FileNotFoundError:
        print(f"Error: No such file named '{filename}' exist!")
        return False


def flatten_json(data, parent_key=None, sep='.'):

    items = {}
    
    if isinstance(data, dict):
        for key, val in data.items():
            full_key = f"{parent_key}{sep}{key}" if parent_key else key
            items.update(flatten_json(val, full_key, sep))
    elif isinstance(data, list):
        for idx, item in enumerate(data):
            full_key = f"{parent_key}{sep}{idx}" if parent_key else str(idx)
            items.update(flatten_json(item, full_key, sep))
    else:
        items[parent_key] = data

    return items

def main():
    print("Hello!")

    data = load_json(INPUT_FILE)

    if data is False:
        return False
    
    flattened = flatten_json(data)

    with open(OUTPUT_FILE, 'w', encoding="utf-8") as f:
        json.dump(flattened, f, indent=2)

    print(f"Saved the flattened JSON to file '{OUTPUT_FILE}'")

    return True


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    
    main()