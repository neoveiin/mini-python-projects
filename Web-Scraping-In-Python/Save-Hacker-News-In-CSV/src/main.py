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
        print(f"Error: Unable to fetch posts:\n{e}\n")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')

    return soup.select("span.titleline > a")



def main():
    pass


if __name__ == "__main__":
    main()
