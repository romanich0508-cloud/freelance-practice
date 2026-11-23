# Freelance Practice

Мій навчальний репозиторій з Python.

## Що тут є

- hello.py: моя перша програма
- test_requests.py: перевірка бібліотека requests

## як запустити

1. Встановити Python
2. Встановити бібліотеки: pip install -r requirements.txt
3. Запустити: python test_reequests.py

## Парсер книг

Програма збирає з тестового сайту books.toscrape.com назви, ціни й рейтинги всіх 1000 книг та зберігає їх у файл books.csv (відкривається в Excel).

Запуск: python books_parser.py

## Telegram-бот для кав'ярні

Бот із кнопками "Меню", "Адреса" та "Години роботи". Запуск: python cafe_bot.py (потрібен токен бота у файлі .env).

## Звіт в Excel

Скрипт читає books.csv, рахує кількість і середню ціну книг та зберігає звіт у books_report.xlsx. Запуск: python books_report.py