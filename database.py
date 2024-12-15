# database.py
import sqlite3

def init_db():
    # Создание и подключение к базе данных
    conn = sqlite3.connect('career_bot.db')
    cursor = conn.cursor()

    # Создание таблицы для пользователей,если ее еще нет
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        age INTEGER,
                        skills TEXT)''')

    conn.commit()
    conn.close()

# Функция для добавления пользователя в базу данных
def add_user(name, age, skills):
    conn = sqlite3.connect('career_bot.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, age, skills) VALUES (?, ?, ?)", (name, age, skills))
    conn.commit()
    conn.close()