# handlers.py
import telebot
from telebot import types
from database import add_user
from recommendations import get_recommendations

users = {}

def send_welcome(message, bot):
    bot.reply_to(message, "👋 Привет! Я твой персональный бот, который поможет найти новый карьерный путь. Давай начнем наше путешествие к успеху!")
    show_main_menu(message.chat.id, bot)

def show_main_menu(chat_id, bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Начать", "Помощь")
    bot.send_message(chat_id, "✨ Главное меню:", reply_markup=markup)

def start_interview(chat_id, bot):
    msg = bot.send_message(chat_id, "💬 Сначала скажи, как тебя зовут?")
    bot.register_next_step_handler(msg, lambda m: process_name_step(m, bot))  # Передаем bot

def process_name_step(message, bot):
    name = message.text
    users[message.chat.id] = {'name': name}
    msg = bot.send_message(message.chat.id, "🗓️ Сколько тебе лет?")
    bot.register_next_step_handler(msg, lambda m: process_age_step(m, bot))  # Передаем bot

def process_age_step(message, bot):
    age = message.text
    users[message.chat.id]['age'] = age
    msg = bot.send_message(message.chat.id, "💼 Какие у тебя есть навыки? Пожалуйста, перечисли их через запятую (например, программирование, дизайн).")
    bot.register_next_step_handler(msg, lambda m: process_skills_step(m, bot))  # Передаем bot

def process_skills_step(message, bot):
    skills = message.text
    users[message.chat.id]['skills'] = skills
    msg = bot.send_message(message.chat.id, "🏢 Какой тип работы тебя интересует? Например, удаленная работа или работа в офисе.")
    bot.register_next_step_handler(msg, lambda m: process_job_type_step(m, bot))  # Передаем bot

def process_job_type_step(message, bot):
    job_type = message.text
    users[message.chat.id]['job_type'] = job_type
    msg = bot.send_message(message.chat.id, "👥 Какой стиль работы тебе больше подходит? Например, работа в команде или самостоятельная работа.")
    bot.register_next_step_handler(msg, lambda m: process_work_style_step(m, bot))  # Передаем bot

def process_work_style_step(message, bot):
    work_style = message.text
    users[message.chat.id]['work_style'] = work_style
    msg = bot.send_message(message.chat.id, "🎨 Есть ли у тебя какие-либо хобби или интересы, которые могут быть связаны с работой? Например, спорт, музыка или искусство.")
    bot.register_next_step_handler(msg, lambda m: process_hobbies_step(m, bot))  # Передаем bot

def process_hobbies_step(message, bot):
    hobbies = message.text
    users[message.chat.id]['hobbies'] = hobbies
    add_user(users[message.chat.id]['name'], users[message.chat.id]['age'], users[message.chat.id]['skills'])
    recommend_careers(message.chat.id, bot)  # Передаем bot

def recommend_careers(chat_id, bot):
    user_info = users[chat_id]
    recommendations = get_recommendations(user_info)
    
    if recommendations:
        rec_text = "🌟 На основе твоих ответов, я могу предложить следующие карьерные пути:\n\n" + "\n - ".join(recommendations)
    else:
        rec_text = "❗ К сожалению, я не смог найти подходящие рекомендации на основе предоставленной информации. Попробуй ответить на вопросы более подробно и точно!"

    bot.send_message(chat_id, rec_text)
    additional_options(chat_id, bot)  # Передаем bot

def additional_options(chat_id, bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("🌈 Получить больше рекомендаций"), types.KeyboardButton("❌ Закончить разговор"))
    bot.send_message(chat_id, "🤔 Хотите получить больше рекомендаций или закончить разговор? Выберите один из вариантов.", reply_markup=markup)

def process_additional_options(message, bot):
    if message.text == "🌈 Получить больше рекомендаций":
        bot.send_message(message.chat.id, "🔁 Вот ещё несколько вариантов, которые могут вам подойти...")
        # Здесь вы можете добавить дополнительные рекомендации
    else:
        bot.send_message(message.chat.id, "🙏 Спасибо за общение! Если у вас возникнут вопросы или нужен совет, всегда обращайтесь снова.")

def handle_text(message, bot):
    if message.text == "Начать":
        start_interview(message.chat.id, bot)
    elif message.text == "Помощь":
        bot.send_message(message.chat.id, "🆘 Я могу помочь тебе с поиском подходящей карьеры. Просто ответь на несколько вопросов!")
    else:
        bot.send_message(message.chat.id, "🤔 Я не совсем понял. Пожалуйста, выбери один из вариантов меню.")