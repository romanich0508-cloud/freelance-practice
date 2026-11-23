import os
import telebot
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Привіт! я твій перший бот. Напиши мені щось.")

@bot.message_handler(content_types=["text"])
def echo_all (message):
    bot.reply_to(message, "Ти написав: " + message.text)

print("Бот запущений...")
bot.infinity_polling()