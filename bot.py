# bot.py
import telebot
from config import TOKEN
from handlers import *
from database import init_db

bot = telebot.TeleBot(TOKEN)

# Инициализируем базу данных
init_db()

@bot.message_handler(commands=['start'])
def start_command(message):
    send_welcome(message, bot)


@bot.message_handler(func=lambda message: True)
def check_message(message):
    handle_text(message, bot)


# Запуск бота
bot.polling()