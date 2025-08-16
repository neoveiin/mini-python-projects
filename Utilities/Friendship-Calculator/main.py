import os

def calc_friendship_compatibilty_score(name1, name2):
    name1, name2 = name1.lower(), name2.lower()

    shared_letters = set(name1).intersection(set(name2))

    vowels = set('aeiou')

    shared_vowels = shared_letters.intersection(vowels)

    similar_char_position = sum(name1[idx] == name2[idx] for idx in range(min(len(name1), len(name2))))

    score = similar_char_position * 15 + len(shared_vowels) * 10 + len(shared_letters) * 5

    return min(score, 100)

def display_in_box(prompt):
    limit = len(prompt) + 6
    print()
    print("*" * limit)
    print("**", prompt, "**", sep=' ')
    print("*" * limit)

def main():

    while True:
        name1 = input("Enter name of friend 1: ")

        if not name1:
            print("Error: Enter a non empty name\n")
            continue
    
        break

    print()

    while True:
        name2 = input("Enter name of friend 2: ")

        if not name2:
            print("Error: Enter a non empty name\n")
            continue
    
        break

    score = calc_friendship_compatibilty_score(name1, name2)

    print(f"\nFriendship compatibility score: {score}")

    if score > 80:
        prompt = "Your friendship is like Chai and Samosa - made for each other!"
    elif score > 50:
        prompt = "Your friendship is like a Tubelight - sometimes work sometimes not!"
    else:
        prompt = "Well... opposites attract, maybe?"
    
    display_in_box(prompt)

if __name__ == "__main__":

    os.system('cls' if os.name == 'nt' else 'clear')

    main()