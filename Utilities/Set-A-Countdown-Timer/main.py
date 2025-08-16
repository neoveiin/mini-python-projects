from time import sleep

def timer():

    while True:
        try:
            seconds = int(input("⏱️  Set timer (in sec): "))
            if seconds < 1:
                print(f"Error: Value for seconds can't be less than 1. Provided: {seconds}\n")
                continue
            break
        except ValueError:
            print("Error: Enter a valid integer value for timer\n")
            continue
        
    print("\n--- Timer Started ---")
    for i in range(seconds, 0, -1):
        mins, secs = divmod(i, 60)
        time_format = f"{mins:02}:{secs:02}"
        print(f"⏳ {time_format}", end='\r')
        sleep(1)
    print("⏳ 00:00")
    print("--- Time's UP! ---")

if __name__ == "__main__":
    timer()