# recommendations.py

def get_recommendations(user_info):
    recommendations = []

    # Примеры карьерных рекомендаций
    if 'программирование' in user_info.get('skills', '').lower():
        recommendations.append("Рассмотрите возможность стать разработчиком программного обеспечения.")
    if 'дизайн' in user_info.get('skills', '').lower():
        recommendations.append("Попробуйте себя в графическом дизайне или UX/UI дизайне.")
    if 'маркетинг' in user_info.get('skills', '').lower():
        recommendations.append("Станьте маркетологом или специалистом по цифровому маркетингу.")
    
    # Учитываем тип работы
    if user_info.get('job_type') == 'удаленная работа':
        recommendations.append("Рассмотрите возможность работы через интернет на фриланс-платформах.")
    elif user_info.get('job_type') == 'офисная работа':
        recommendations.append("Можно подать заявку на вакансию в офис компании в вашем городе.")

    # Учитываем стиль работы
    if user_info.get('work_style') == 'работа в команде':
        recommendations.append("Подходящие професии могут включать менеджера проектов или координатора.")
    elif user_info.get('work_style') == 'самостоятельная работа':
        recommendations.append("Рассмотрите возможности индивидуального предпринимательства.")

    # Хобби и интересы
    hobbies = user_info.get('hobbies', '').lower()
    if 'живопись' in hobbies or 'арт' in hobbies:
        recommendations.append("Исследуйте возможности карьеры в искусстве или арт-терапии.")
    if 'музыка' in hobbies:
        recommendations.append("Станьте музыкантом или звуковым дизайнером.")
    if 'спорт' in hobbies:
        recommendations.append("Рассмотрите карьеру в фитнес-менеджменте или спортивной аналитике.")
    if 'наука' in hobbies:
        recommendations.append("Работа в сфере науки, такой как исследователь или аналитик данных, может быть вам интересна.")

    # Добавляйте дополнительные условия для других навыков и предпочтений

    return recommendations