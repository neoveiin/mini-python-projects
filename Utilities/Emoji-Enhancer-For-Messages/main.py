def enhance_msg():

    emotions = {
        "happy": "😊",
        "sad": "😢",
        "angry": "😡",
        "surprised": "😲",
        "love": "❤️",
        "laughing": "😂",
        "confused": "😕",
        "cool": "😎",
        "tired": "😴",
        "worried": "😟",
        "crying": "😭",
        "party": "🥳",
        "thinking": "🤔",
        "shy": "☺️",
        "scared": "😱",
        "sick": "🤒",
        "nerdy": "🤓",
        "blush": "😳",
        "starstruck": "🤩"
    }

    msg = input("Enter a message to enhance: ").strip()

    words = msg.split()

    new_msg = []

    for word in words:
        if word.isalpha():
            if word.lower() in emotions:
                new_msg.append(f"{word} {emotions[word]}")
            else:
                new_msg.append(word)
        else:
            if word[:-1].isalpha():
                if word[:-1].lower() in emotions:
                    new_msg.append(f"{word[:-1]} {emotions[word[:-1]]}{word[-1]}")
                else:
                    new_msg.append(word)
    
    new_msg = " ".join(new_msg)

    print(f"\nEnhanced message: {new_msg}")

enhance_msg()