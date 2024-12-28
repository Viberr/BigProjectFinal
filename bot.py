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

#@bot.callback_query_handler(func=lambda message: message.text == "1")
#def check_valid(message):
    #handle_invalid_request(message, bot)

# Запуск бота
bot.polling()