import os
import json
import sys

FILENAME = "movies.json"

# utility functions
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_str(prompt, error_msg, attempts=None):

    if not attempts:
        while True:
            val = input(prompt).strip()
            if not val:
                print(f"{error_msg}\n")
                continue
            return val
    else:
        for i in range(attempts):
            val = input(prompt).strip()
            if not val:
                print(f"{error_msg}\n")
                continue
            return val
        else:
            print("Attempts exhausted. Try again...")
            hold()
            return False

def hold():
    input("\nPress Enter to continue...")

def initialize_db():
    if not os.path.isfile(FILENAME):
        with open(FILENAME, 'w', encoding='utf-8') as f:
            json.dump([], f)
            return
    
    with open(FILENAME, 'r', encoding='utf-8') as f:
        movies = json.load(f)
        
        do_overwrite = False

        prompt = ("There already exists a corrupted database.\n"
                  "Would you like to overwrite it and create a fresh one (y/n)? "
                  )
        
        if isinstance(movies, list):
            if not movies:
                return

            are_valid_movies = all(
                isinstance(movie, dict) and list(movie.keys()) == ["title", "genre", "rating"]
                for movie in movies
            )

            if are_valid_movies:
                return
            else:
                overwrite = input(prompt).strip().lower()

                if overwrite == "y":
                    do_overwrite = True
        else:
            overwrite = input(prompt).strip().lower()

            if overwrite == "y":
                do_overwrite = True
        
        if do_overwrite:
            with open(FILENAME, 'w', encoding='utf-8') as f:
                json.dump([], f)
                clear_screen()
                return
        
        print("Operation aborted! Thanks for using MoviesDB!")
        sys.exit(1)

def load_movies():
    with open(FILENAME, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_movies(movies):
    with open(FILENAME, 'w', encoding='utf-8') as f:
        json.dump(movies, f, indent=2)

def add_movie(movies):

    clear_screen()
    
    while True:
        title = get_str(
            "Enter movie title: ",
            "Error: Enter a non empty movie title",
            3
        )

        if title is False:
            return

        if any(
            movie["title"].lower() == title.lower()
            for movie in movies
        ):
            print(f"Error: Movie: {title}, already exists! Try updating it...")
            return
        
        break

    genre = get_str(
        "Enter genre: ",
        "Error: Enter a non empty genre",
        3
    )

    if genre is False:
        return

    for _ in range(3):
        rating = input("Enter rating (0-10): ")
        
        if not rating.isdigit() or not (0 <= int(rating) <= 10):
            print("Error: Enter a numerical value between 0 and 10 only\n")
            continue

        break
    else:
        print("Attempts exhausted. Try again...")
        hold()
        return

    movies.append({"title": title, "genre": genre, "rating": rating})

    save_movies(movies)

    print(f"\nMovie: {title}, got successfully added!")

    hold()

def view_movies(movies):

    clear_screen()

    if not movies:
        print("No movies to display!")
        hold()
        return
    
    print("Movies List")

    # Find column widths dynamically
    title_width = max(len(m["title"]) for m in movies + [{"title": "title"}])
    genre_width = max(len(m["genre"]) for m in movies + [{"genre": "genre"}])
    rating_width = max(len(str(m["rating"])) for m in movies + [{"rating": "rating"}])

    # Build a row format string
    row_format = f"| {{:<{title_width}}} | {{:<{genre_width}}} | {{:<{rating_width}}} |"

    # Top border
    total_width = title_width + genre_width + rating_width + 10  # 10 for the separators and spaces
    print("-" * total_width)

    # Header row
    print(row_format.format("title", "genre", "rating"))

    # Separator
    print("-" * total_width)

    # Data rows
    for movie in movies:
        print(row_format.format(movie["title"], movie["genre"], movie["rating"]))

    # Bottom border
    print("-" * total_width)

    hold()

def title_exists(title, movies):
    return any(
        movie["title"].lower() == title.lower()
        for movie in movies
    )

def update_movie(movies):

    clear_screen()

    if not movies:
        print("No movies to update!")
        hold()
        return
    
    title = get_str(
        "Enter title of movie, you want to update: ",
        "Error: Enter a non empty movie title",
        3
    )

    if title is False:
        return

    if not title_exists(title, movies):
        print(f"Error: There's no such movie '{title}'. Try again...")
        hold()
        return
    
    print("\nInstructions: Only enter value when you want to update else leave blank.")
    new_title = get_str(
        "Enter new title: ",
        "Error: Enter a valid movie title",
        3
    )

    if new_title is False:
        return
    
    new_genre = get_str(
        "Enter new genre: ",
        "Error: Enter a valid movie title",
        3
    )

    if new_genre is False:
        return

    for _ in range(3):
        new_rating = input("Enter new rating (0-10): ")
        
        if not new_rating.isdigit() or not (0 <= int(new_rating) <= 10):
            print("Error: Enter a numerical value between 0 and 10 only\n")
            continue

        break
    else:
        print("Attempts exhausted. Try again...")
        hold()
        return

    if not new_title and not new_genre and not new_rating:
        print("Since, no vlaues are provided. Updation didn't take place!")
        hold()
        return
    
    for movie in movies:
        if movie["title"].lower() == title:
            print("Changes: ")
            if new_title:
                print(f"{movie["title"]} -> {new_title}")
                movie["title"] = new_title
            if new_genre:
                print(f"{movie["genre"]} -> {new_genre}")
                movie["genre"] = new_genre
            if new_rating:
                print(f"{movie["rating"]} -> {new_rating}")
                movie["rating"] = new_rating
            break
    
    save_movies(movies)

    print("Updation took place successfully!")

    hold()

def delete_movie(movies):
    clear_screen()

    if not movies:
        print("No movies to delete!")
        hold()
        return

    title = get_str(
        "Enter title of movie, you want to delete: ",
        "Error: Enter a non empty movie title",
        3
    )

    if title is False:
        return

    if not title_exists(title, movies):
        print(f"\nError: There's no such movie '{title}'. Try again...")
        hold()
        return

    for idx, movie in enumerate(movies):
        if movie["title"].lower() == title.lower():
            deleted_movie = movies.pop(idx)
            print("\nDetails of deleted movie:")
            for label, val in deleted_movie.items():
                print(f"{label}: {val}")
            break

    save_movies(movies)

    print("\nDeletion tool place succesfully!")

    hold()

def search_movies(movies):
    clear_screen()

    if not movies:
        print("No movies to search!")
        hold()
        return

    keyword = get_str(
        "Enter a keyword: ",
        "Error: Enter a non empty keyword",
        3
    )

    if keyword is False:
        return

    search_results = [
        movie
        for movie in movies
        if keyword.lower() in movie["title"].lower() or keyword.lower() in movie["genre"].lower()
    ]

    if not search_results:
        print("\nNo movies found!")
        hold()
        return

    view_movies(search_results)

def main():

    initialize_db()

    movies = load_movies()

    while True:

        clear_screen()

        print("--- MovieDB Menu ---")
        print(
            "1. Add movie\n"
            "2. View all movies\n"
            "3. Update movie\n"
            "4. Delete movie\n"
            "5. Search a movie (by title or genre)\n"
            "6. Exit"
        )
        choice = get_str(
            "Enter a choice (1-6): ",
            "Error: Enter a valid choice"
        )

        match choice:
            case '1':
                add_movie(movies)
            case '2':
                view_movies(movies)
            case '3':
                update_movie(movies)
            case '4':
                delete_movie(movies)
            case '5':
                search_movies(movies)
            case '6':
                print("\nThanks for using MoviesDB!")
                break
            case _:
                print("\nError: Enter a valid choice between 1 and 6. Provided: '{choice}'")
                continue

if __name__ == "__main__":
    main()
