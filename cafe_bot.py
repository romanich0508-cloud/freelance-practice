import os
import telebot
from telebot import types
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

def main_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("☕ Меню", "📍 Адреса")
    keyboard.add("🕒 Години роботи")
    keyboard.add("📞 Контакти")
    return keyboard
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "Вітаємо в кав'ярні «Зерно»! Оберіть, що вас цікавить:",
        reply_markup=main_keyboard(),
    )
@bot.message_handler(commands=["help"])
def send_helper(message):
    bot.send_message(
        message.chat.id,
        "Вітаємо! Раді бачити вас у нашому боті. Тут можна легко переглянути актуальне меню, дізнатися графік роботи, знайти нашу адресу та зберегти контакти для зв'язку. Обирайте, що цікавить!",
        reply_markup=main_keyboard(),
    )
@bot.message_handler(content_types=["text"])
def handle_text(message):
    text = message.text

    if text == "☕ Меню":
        answer = "Еспресо: 50 грн\nКапучино: 70 грн\nЛатте: 75 грн\nЧізкейк: 90 грн"
    elif text == "📍 Адреса":
        answer = "Вул. Львівська, 1"
    elif text == "🕒 Години роботи":
        answer = "Щодня з 8:00 до 21:00"
    elif text == "📞 Контакти":
        answer = "+380 00 000 0000" 
    else:
        answer = "Натисніть одну з кнопок нижче 👇"

    bot.send_message(message.chat.id, answer, reply_markup=main_keyboard())

print("Бот запущений ...")
bot.infinity_polling()