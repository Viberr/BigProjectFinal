# bot.py
import telebot
from config import TOKEN
from handlers import send_welcome
from database import init_db

bot = telebot.TeleBot(TOKEN)

# Инициализируем базу данных
init_db()

@bot.message_handler(commands=['start'])
def start_command(message):
    send_welcome(message, bot)

# Запуск бота
bot.polling()