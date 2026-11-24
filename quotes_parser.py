import csv
import time
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://quotes.toscrape.com/page/-{}"

result = []

for page_number in range(1, 11):
    url = BASE_URL.format(page_number)
  
    response = requests.get(url)
    response.encoding = "utf-8"

    if response.status_code != 200:
        print("Не вдалося відкрити сторінку", page_number)
        break

    page = BeautifulSoup(response.text, "html.parser")

    quotes = page.select("div.quote")

    for quote in quotes:
        tag_texts = []
        words = quote.select_one("span.text").text
        tags = quote.select("a.tag")
        for tag in tags:
            tag_texts.append(tag.text)
        line = ", ".join(tag_texts)
        author = quote.select_one("small.author").text
        result.append([words, line, author ])

    print("Сторінка", page_number, "готова")
    time.sleep(0.5)

with open("quotes.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Слова", "Теги", "Автор"])
    writer.writerows(result)

print("Готово! Збережено цитат:", len(result))