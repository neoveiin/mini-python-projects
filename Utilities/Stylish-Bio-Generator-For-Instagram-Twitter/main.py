def bio_generator():
    name = input("What's your name: ").strip()
    profession = input("What's your profession: ").strip()
    passion = input("What's your passion (one-liner): \n").strip()
    emoji = input("What's your favourite emoji: ").strip()
    website = input("Enter your website or handle: ").strip()

    print("\nBio Styles to choose from:")
    print("1. One Liner")
    print("2. Multi-line")
    print("3. Emoji sandwich")

    style = input("Enter 1, 2 or 3: ")

    match style:
        case "1":
            bio = f"{emoji} {name} > {profession} > {passion} | {website} {emoji}"
        case "2":
            bio = f"{emoji} {name} | {profession}\n🔥 {passion}\n🔗 {website}"
        case "3":
            count = len(max(f"{emoji} {name} | {profession}", website))
            bio = f"{emoji*(count//2)}\n👤 {name} | {profession}\n🔥 {passion}\n🔗 {website}\n{emoji*(count//2)}"
    
    print(f"\n{'-' * 15}\n{bio}\n{'-' * 15}\n")

    user = input("Would you like to save this bio in a .txt file? (y/n): ").strip().lower()

    if user == "y":
        filename = f"{name.replace(' ', '_')}_bio.txt"

        with open(filename, "w") as f:
            f.write(bio)
        
        print(f"Successfully saved your bio to '{filename}'.")

if __name__ == "__main__":
    
    bio_generator()