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
                        skills TEXT,
                        job_type TEXT,
                        work_style TEXT,
                        hobbies TEXT
                    )''')

    conn.commit()
    conn.close()

# Функция для добавления пользователя в базу данных
def add_user(name, age, skills, job_type, work_style, hobbies):
    conn = sqlite3.connect('career_bot.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, age, skills, job_type, work style, hobbies) VALUES (?, ?, ?)", (name, age, skills, job_type, work_style, hobbies))
    conn.commit()
    conn.close()