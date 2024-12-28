# handlers.py
import telebot
from telebot import types
from database import add_user
from recommendations import get_recommendations
 

users = {}

def send_welcome(message, bot):
    bot.reply_to(message, "👋 Привет! Я твой персональный бот, который поможет найти новый карьерный путь. Давай начнём наше путешествие к успеху!")
    show_main_menu(message.chat.id, bot)

def show_main_menu(chat_id, bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Начать", "Помощь", "Профиль", "Контакты для обратной связи")
    bot.send_message(chat_id, "✨ Главное меню:", reply_markup=markup)

def start_interview(chat_id, bot):
    msg = bot.send_message(chat_id, "💬 Сначала скажи, как тебя зовут?")
    bot.register_next_step_handler(msg, lambda m: process_name_step(m, bot))

def process_name_step(message, bot):
    name = message.text
    users[message.chat.id] = {'name': name}
    msg = bot.send_message(message.chat.id, "🗓️ Сколько тебе лет?")
    bot.register_next_step_handler(msg, lambda m: process_age_step(m, bot))

def process_age_step(message, bot):
    age = message.text
    users[message.chat.id]['age'] = age
    msg = bot.send_message(message.chat.id, "💼 Какие у тебя есть навыки? Пожалуйста, перечисли их через запятую (например, программирование, дизайн).")
    bot.register_next_step_handler(msg, lambda m: process_skills_step(m, bot))

def process_skills_step(message, bot):
    skills = message.text
    users[message.chat.id]['skills'] = skills
    msg = bot.send_message(message.chat.id, "🏢 Какой тип работы тебя интересует? Например, удаленная работа или работа в офисе.")
    #handle_invalid_request(skills)
    bot.register_next_step_handler(msg, lambda m: process_job_type_step(m, bot))

def process_job_type_step(message, bot):
    job_type = message.text
    users[message.chat.id]['job_type'] = job_type
    msg = bot.send_message(message.chat.id, "👥 Какой стиль работы тебе больше подходит? Например, работа в команде или самостоятельная работа.")
    #handle_invalid_request(job_type)
    bot.register_next_step_handler(msg, lambda m: process_work_style_step(m, bot))

def process_work_style_step(message, bot):
    work_style = message.text
    users[message.chat.id]['work_style'] = work_style
    msg = bot.send_message(message.chat.id, "🎨 Есть ли у тебя какие-либо хобби или интересы, которые могут быть связаны с работой? Например, спорт, музыка или искусство.")
    #handle_invalid_request(work_style)
    bot.register_next_step_handler(msg, lambda m: process_hobbies_step(m, bot))

def process_hobbies_step(message, bot):
    hobbies = message.text
    users[message.chat.id]['hobbies'] = hobbies

    # Собираем всю информацию и сохраняем ее в БД
    add_user(
        users[message.chat.id]['name'],
        users[message.chat.id]['age'],
        users[message.chat.id]['skills'],
        users[message.chat.id]['job_type'],
        users[message.chat.id]['work_style'],
        users[message.chat.id]['hobbies']
    )

    recommend_careers(message.chat.id, bot)

def recommend_careers(chat_id, bot):
    user_info = users[chat_id]
    recommendations = get_recommendations(user_info)

    if recommendations:
        rec_text = "🌟 На основе твоих ответов, я могу предложить следующие карьерные пути:\n\n" + "\n - ".join(recommendations)
    else:
        rec_text = "❗ К сожалению, я не смог найти подходящие рекомендации на основе предоставленной информации. Попробуй ответить на вопросы более подробно и точно!"

    bot.send_message(chat_id, rec_text)
    additional_options(chat_id, bot)

def additional_options(chat_id, bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🌈 Получить больше рекомендаций", "Изменить ответы", "❌ Закончить разговор")
    bot.send_message(chat_id, "🤔 Что вы хотите сделать дальше?", reply_markup=markup)


def handle_text(message, bot):
    if message.text == "Начать":
        start_interview(message.chat.id, bot)
    elif message.text == "Помощь":
        bot.send_message(message.chat.id, "🆘 Я могу помочь тебе с поиском подходящей карьеры. Просто ответь на несколько вопросов!")
    elif message.text == "🌈 Получить больше рекомендаций":
        recommend_careers(message.chat.id, bot)  # Повторно предложить рекомендации
    elif message.text == "Изменить ответы":
        bot.send_message(message.chat.id, "📝 Пожалуйста, начните заново, выбрав «Начать» в главном меню.")
        show_main_menu(message.chat.id, bot)
    elif message.text == "Профиль":
        user = users.get(message.chat.id)
        if user:
            profile_info = f"👤 Имя: {user['name']}\n📅 Возраст: {user['age']}\n💼 Навыки: {user['skills']}\n🏢 Тип работы: {user['job_type']}\n👥 Стиль работы: {user['work_style']}\n🎨 Хобби: {user['hobbies']}"
            bot.send_message(message.chat.id, profile_info)
        else:
            bot.send_message(message.chat.id, "❗ Профиль отсутствует. Пожалуйста, начните с «Начать».")
    elif message.text == "Контакты для обратной связи":
        bot.send_message(message.chat.id, "📧 Вы можете связаться с нами по адресу: support@example.com")
    elif message.text == "❌ Закончить разговор":
        bot.send_message(message.chat.id, "🙏 Спасибо за общение! Если у вас возникнут вопросы или нужен совет, всегда обращайтесь снова.")
        show_main_menu(message.chat.id, bot)  # Вернуться в главное меню
    else:
        bot.send_message(message.chat.id, "🤔 Я не совсем понял. Пожалуйста, выбери один из вариантов меню.")

#РЕДАКТИРОВАТЬ
#def handle_invalid_request (message, bot):
    #if message.text not in get_recommendations:
        #bot.send_message(message.chat.id, "🤔 Я не совсем понял. Возможно вы совершили ошибку в написании, либо такого ответа ещё нету в нашей программе")

    
    

