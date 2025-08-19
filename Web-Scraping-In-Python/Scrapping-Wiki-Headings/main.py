import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/NASA"

def get_h2_headers(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch page: {e}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")

    h2_tags = soup.find_all("h2")

    h2_headings = []

    exceptions = ["Contents", "Bibliography", "See also", "References", "Further reading", "External links"]

    for h2 in h2_tags:
        if (h2_heading_text := h2.get_text(strip=True)) not in exceptions:
            h2_headings.append(h2_heading_text)
    
    return h2_headings

print(get_h2_headers(URL))