import vk_api

def get_user_info(vk, user_id):
    try:
        user_info = vk.users.get(user_ids=user_id, fields="activities, bdate, city, country, home_town, photo_id, status, sex, contacts, education, interests, followers_count")[0]
        return user_info
    except Exception as e:
        print("Ошибка получения информации о пользователе:", e)
        return None

def get_user_groups(vk, user_id):
    try:
        groups = vk.groups.get(user_id=user_id, extended=1)
        return groups['items']
    except Exception as e:
        print("Ошибка получения групп:", e)
        return []

def get_user_posts(vk, user_id):
    try:
        posts = vk.wall.get(owner_id=user_id, count=10)
        return posts['items']
    except Exception as e:
        print("Ошибка получения записей:", e)
        return []

def main():
    token = 'ad6148f2ad6148f2ad6148f2a9ae40ec1daad61ad6148f2ca7a224fce685d62665a4360'  # Замените на ваш токен
    user_token ='vk1.a.bXS6FJiOxeqAOtdp9HJbgAaQpQdIHkHxkAg0bAj55Vih3wHUr88fM-3AItO7VDpZu7xQziKY3tUpka7xKo-ILPV8aQkM2LWHLAOaJNT_SY99MsL_S6l7LoGlMhiDK2GhlyC1iUWWIHttc1p5RDxYunYIMcZF9Is99nXzFk--OkxLDduh3sQAkHPEpzse2UdLF1cPz4-4o3ypfQPKQfDFow'
    # Авторизация с помощью vk_api
    vk_session = vk_api.VkApi(token='ad6148f2ad6148f2ad6148f2a9ae40ec1daad61ad6148f2ca7a224fce685d62665a4360')
    vk_u_sess = vk_api.VkApi(token=user_token)
    vk = vk_session.get_api()
    vk_us = vk_u_sess.get_api()
    user_id = input("Введите ID пользователя или его никнейм: ")

    # Получение информации о пользователе
    user_info = get_user_info(vk, user_id)
    if user_info:
        print("Информация о пользователе:")
        print(f"ID: {user_info['id']}")
        print(f"Имя: {user_info['first_name']}")
        print(f"Фамилия: {user_info['last_name']}")
        print(f"Дата рождения: {user_info.get('bdate', 'Не указана')}")
        print(f"Пол: {'Мужской' if user_info['sex'] == 2 else 'Женский' if user_info['sex'] == 1 else 'Не указан'}")
        print(f"Город: {user_info.get('city', {}).get('title', 'Не указан')}")
        print(f"Страна: {user_info.get('country', {}).get('title', 'Не указана')}")
        print(f"Фото: {user_info.get('photo_id', 'Нет')}")
        print(f"Статус: {user_info.get('status', 'Нет')}")
        
        # Получение групп пользователя
        groups = get_user_groups(vk_us, user_info['id'])
        print("\nГруппы пользователя:")
        for group in groups:
            print(f"ID: {group['id']}, Название: {group['name']}")

        # Получение записей на стене
        posts = get_user_posts(vk_us, user_info['id'])
        print("\nЗаписи на стене пользователя:")
        for post in posts:
            print(f"ID поста: {post['id']}, Дата: {post['date']}, Текст: {post['text']}")
    
if __name__ == "__main__":
    main()
    input()
    
