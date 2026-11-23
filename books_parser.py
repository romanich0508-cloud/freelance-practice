import csv
import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"

# 1. Відкриваємо сторінку
response = requests.get(URL)
response.encoding = "utf-8"

# 2. Віддаємо текст сторінки "читачу"
page = BeautifulSoup(response.text, "html.parser")

# 3. Знаходимо всі картки з книгами
books = page.select("article.product_pod")

# 4. З кожної картки беремо назву й ціну
result = []
for book in books:
    title = book.h3.a["title"]
    price = book.select_one("p.price_color").text
    result.append([title, price])
    print(title, "-", price)

# 5. Зберігаємо в файл, який відкривається в Excel
with open("books.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Назва", "Ціна"])
    writer.writerows(result)

print("Готово! Збережено книг:", len(result))