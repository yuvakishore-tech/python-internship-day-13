import requests
from bs4 import BeautifulSoup
import csv

URL = "https://quotes.toscrape.com/"

response = requests.get(URL)

if response.status_code != 200:
    print("Failed to fetch page")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

quotes_data = []

quotes = soup.find_all("div", class_="quote")

for quote in quotes:
    text = quote.find("span", class_="text")
    author = quote.find("small", class_="author")
    tags = quote.find_all("a", class_="tag")

    quotes_data.append({
        "quote": text.get_text() if text else "N/A",
        "author": author.get_text() if author else "N/A",
        "tags": ", ".join(tag.get_text() for tag in tags) if tags else "N/A"
    })

with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["quote", "author", "tags"])
    writer.writeheader()
    writer.writerows(quotes_data)

print("Data scraped and saved to quotes.csv")
