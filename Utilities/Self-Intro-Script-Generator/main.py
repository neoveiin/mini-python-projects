from datetime import date

def self_intro():
    name = input("What's your name? ").strip()
    age = input("How old are you? ").strip()
    city = input("Where do you live? ").strip()
    profession = input("What's your profession? ").strip()
    hobby = input("What's your favourite hobby? ").strip()

    current_date = date.today().isoformat()

    intro = (
        f"Hello! My name is {name}. I'm {age} years old and I live in {city} city. "
        f"I work as a {profession} and I absolutely enjoy {hobby} in my free time."
    )

    border = "-" * len(intro)

    intro += f"\nNice to meet you!\n\nLogged on: {current_date}"

    return f"\n{border}\n{intro}\n{border}\n"

if __name__ == "__main__":
    print(self_intro())