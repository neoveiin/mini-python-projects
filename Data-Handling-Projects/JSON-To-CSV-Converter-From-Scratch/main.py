import json, csv, os

def json_to_csv(input_json_file, output_csv_file):
    try:
        with open(input_json_file, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print(f"Error: Invalid JSON file! Try again...")
                return False
            
            if not data:
                print("Error: There is no data to fetch from the API call. Try again...")
                return False
    except FileNotFoundError:
        print(f"Error: No such file named '{input_json_file}' exists. Try again...")
        return False
    
    headers = list({
        key
        for record in data
        for key in record
    })

    print("--- Fields in JSON file ---")
    for sr_no, header in enumerate(headers, 1):
        print(f"{sr_no}. {header.title()}")
    
    while True:
        choices = input(f"\nEnter choices separated by comma (1, 2, ..): ").strip().strip(',')
        choices = {choice.strip() for choice in choices.split(',')}

        if not all(
            choice.isdigit()
            for choice in choices
        ):
            print(f"Error: Enter valid choices only. Invalid choices: {', '.join(
                choice
                for choice in choices
                if not choice.isdigit()
            )}\n")
            continue
    
        if not all(
            1 <= int(choice) <= len(headers)
            for choice in choices
        ):
            print(f"Error: Enter valid choices only. Out of range choices: {', '.join(
                choice
                for choice in choices
                if not (1 <= int(choice) <= len(headers))
            )}\n")
            continue

        break
    
    headers = [
        headers[int(choice)-1]
        for choice in choices
    ]


    with open(output_csv_file, 'w', newline='', encoding='utf-8') as f:
        wo = csv.writer(f)

        wo.writerow(headers)

        no_of_records = 0

        for record in data:
            
            if not all(
                True if header in record else False
                for header in headers
            ):
                continue



            wo.writerow([
                record.get(header)
                for header in headers
            ])

            no_of_records += 1
        
    print(f"\nSelected headers: {', '.join(headers)} from JSON file: '{input_json_file}' are successfuly parsed into the CSV file: '{output_csv_file}'")
    print(f"\nTotal no of records converted: {no_of_records}")

    return True

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')

    json_to_csv("api_data.json", "converted_data.csv")