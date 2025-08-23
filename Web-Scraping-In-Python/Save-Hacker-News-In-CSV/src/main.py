import csv
import requests
from bs4 import BeautifulSoup


HN_URL = "https://news.ycombinator.com/"
EXPORT_FILENAME = "hn_top20.csv"


def fetch_posts():
    try:
        response = requests.get(HN_URL, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"\nError: Unable to fetch posts:\n{e}\n")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')

    return soup.select("span.titleline > a")


def save_to_csv(posts):

    if not posts:
        print("No posts to save!")
        return
    
    posts_to_save = []

    for post in posts[:20]:
        posts_to_save.append({
            "url": post['href'],
            "title": post.text
        })
    
    with open(EXPORT_FILENAME, 'w', newline='', encoding="utf-8") as f:
        wo = csv.DictWriter(f, fieldnames=["url", "title"])
        wo.writeheader()

        wo.writerows(posts_to_save)

    print(F"Done! Posts from Hacker News are exported to '{EXPORT_FILENAME}'.")
    return


def main():
    print("Fetching posts...")
    posts = fetch_posts()
    save_to_csv(posts)


if __name__ == "__main__":
    main()
