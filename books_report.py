import csv
from openpyxl import Workbook
from openpyxl.styles import Font

def get_price(book):
    return book["price"]

books = []

with open("books.csv", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    for row in reader:
        price = float(row["Ціна"].replace("£", ""))
        books.append({
            "title": row["Назва"],
            "price": price,
            "rating": row["Рейтинг"],
        })
total_price = 0
for book in books:
    total_price += book["price"]
average_price = total_price / len(books)
sorted_books = sorted(books, key=get_price)
cheapest = sorted_books[0]
most_expensive = sorted_books[-1]

workbook = Workbook()

summary = workbook.active
summary.title = "Підсумок"
summary["A1"] = "Усього книг"
summary["B1"] = len(books)
summary["A2"] = "Середня ціна (£)"
summary["B2"] = round(average_price, 2)
summary["A3"] = "Найдешевша книга"
summary["B3"] = cheapest["title"]
summary["A4"] = "Найдорожча книга"
summary["B4"] = most_expensive["title"]
summary.column_dimensions["A"].width = 22
summary.column_dimensions["B"].width = 60 

top = workbook.create_sheet("10 найдешевших")
top.append(["Назва", "Ціна (£)", "Рейтинг"])
for book in sorted_books[:10]:
    top.append([book["title"], book["price"], book["rating"]])

for cell in top[1]:
    cell.font = Font(bold=True)
top.column_dimensions["A"].width = 60

books_by_rating = workbook.create_sheet("Кількість книг за рейтингом")
books_by_rating.append(["Рейтинг", "Кількість"])
counts = {}
for book in books:
    if book["rating"] in counts:
        counts[book["rating"]] += 1
    else:
        counts[book["rating"]] = 1
for key, value in counts.items():
    books_by_rating.append([key, value])

workbook.save("books_report.xlsx")
print("Готово! файл books_report.xlsx створено.")