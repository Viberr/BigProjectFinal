# recommendations.py

def get_recommendations(user_info):
    recommendations = []

    # Определяем маппинг рекомендаций
    skills_recommendations = {
        'программирование': "Рассмотрите возможность стать разработчиком программного обеспечения.",
        'дизайн': "Попробуйте себя в графическом дизайне или UX/UI дизайне.",
        'маркетинг': "Станьте маркетологом или специалистом по цифровому маркетингу.",
        'проектный менеджмент': "Рассмотрите карьеру менеджера проектов или координатора.",
        'продажи': "Изучите карьерные возможности в области продаж или бизнеса.",
        'аналитика': "Откройте для себя карьеру в аналитике данных или бизнес-аналитике.",
        'журналистика': "Попробуйте себя как журналист или контент-менеджер.",
        'искусство': "Изучите возможности в искусстве или арт-терапии.",
        'учительство': "Станьте учителем или репетитором.",
        'финансовый анализ': "Рассмотрите карьеру финансового аналитика."
    }

    # Проверяем навыки на рекомендации
    user_skills = user_info.get('skills', '').lower()
    for skill, recommendation in skills_recommendations.items():
        if skill in user_skills:
            recommendations.append(recommendation)

    # Учитываем тип работы
    job_type_recommendations = {
        'удаленная работа': "Рассмотрите возможность работы через интернет на фриланс-платформах.",
        'офисная работа': "Можно подать заявку на вакансию в офис компании в вашем городе.",
        'гибридная работа': "Ищите вакансии, предлагающие гибридный формат работы."
    }

    job_type = user_info.get('job_type')
    if job_type in job_type_recommendations:
        recommendations.append(job_type_recommendations[job_type])

    # Учитываем стиль работы
    work_style_recommendations = {
        'работа в команде': "Подходящие профессии могут включать менеджера проектов, координатора или разработчика в команде.",
        'самостоятельная работа': "Рассмотрите возможности индивидуального предпринимательства или фриланса."
    }

    work_style = user_info.get('work_style')
    if work_style in work_style_recommendations:
        recommendations.append(work_style_recommendations[work_style])

    # Хобби и интересы
    hobbies_recommendations = {
        'живопись': "Исследуйте возможности карьеры в искусстве, картинной галерее или арт-терапии.",
        'музыка': "Станьте музыкантом, звуковым дизайнером или продюсером.",
        'спорт': "Рассмотрите карьеру в фитнес-менеджменте, спортивной аналитике или тренерстве.",
        'наука': "Работа в сфере науки, как исследователь или аналитик данных, может быть вам интересна.",
        'технологии': "Ищите карьеры, связанные с новыми технологиями, такими как IT или кибербезопасность.",
        'путешествия': "Рассмотрите карьеру в туризме, как турагент или менеджер по туризму.",
        'видеография': "Станьте видеографом, монтажером или специалистом по контенту для видеоплатформ."
    }

    user_hobbies = user_info.get('hobbies', '').lower()
    for hobby, recommendation in hobbies_recommendations.items():
        if hobby in user_hobbies:
            recommendations.append(recommendation)

    # Новые рекомендации на основе ответов пользователя
    job_preference = user_info.get('job_preference')
    if job_preference == 'высокий доход':
        recommendations.append("Рассмотрите профессии в таких сферах, как финансовый анализ или программирование, которые могут предложить высокий доход.")
    if job_preference == 'творчество':
        recommendations.append("Сфокусируйтесь на креативных профессиях, таких как графический дизайнер или маркетолог.")
    if job_preference == 'стабильность':
        recommendations.append("Работа в государственных учреждениях или крупных корпорациях может обеспечить большую стабильность.")

    # Комбинации рекомендаций
    if 'программирование' in user_skills and 'удаленная работа' in job_type:
        recommendations.append("Рассмотрите удаленные вакансии разработчика программного обеспечения.")
    
    if 'дизайн' in user_skills and 'работа в команде' in work_style:
        recommendations.append("Командная работа в дизайнерской студии может быть отличным вариантом для вас.")
    
    if 'анализ' in user_skills and 'наука' in user_hobbies:
        recommendations.append("Карьерный путь аналитика в научной области может быть вам интересен.")

    if 'музыка' in user_hobbies and 'офисная работа' in job_type:
        recommendations.append("Вы можете рассмотреть работу в сфере медиапланирования или в музыкальной компании.")

    return recommendations