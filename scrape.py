import requests
from bs4 import BeautifulSoup

def scrape_url_text(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")
    for tag in soup(["script", "style"]): tag.decompose()
    return "\n".join(line.strip() for line in soup.get_text().splitlines() if line.strip())
