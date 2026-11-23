import csv
import time
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

result = []

for page_number in range(1, 51):
    url = BASE_URL.format(page_number)

    response = requests.get(url)
    response.encoding = "utf-8"

    if response.status_code != 200:
        print("Не вдалося відкрити сторінку", page_number)
        break

    page = BeautifulSoup(response.text, "html.parser")

    books = page.select("article.product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.select_one("p.price_color").text
        rating = book.select_one("p.star-rating")["class"][1]
        result.append([title, price, rating])
       
    print("Сторінка", page_number, "готова")
    time.sleep(0.5)

with open("books.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Назва", "Ціна", "Рейтинг"])
    writer.writerows(result)

print("Готово! Збережено книг:", len(result))