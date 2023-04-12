# Импортируем библиотеку для работы с VK API
import vk_api

# Открываем файл с логинами и паролями аккаунтов
with open("accounts.txt", "r") as f:
    # Считываем каждую строку в список
    accounts = f.readlines()

# Открываем файл с ID пользователей, которым нужно отправить сообщения
with open("users.txt", "r") as f:
    # Считываем каждую строку в список
    users = f.readlines()

# Задаем текст сообщения
message = "Привет! Это тестовое сообщение от бота."

# Для каждого аккаунта в списке
for account in accounts:
    # Разделяем логин и пароль по пробелу
    login, password = account.split()
    # Создаем объект для работы с VK API
    vk_session = vk_api.VkApi(login, password)
    # Пытаемся авторизоваться
    try:
        vk_session.auth()
        # Получаем объект для отправки сообщений
        vk = vk_session.get_api()
        # Для каждого пользователя в списке
        for user in users:
            # Отправляем сообщение
            vk.messages.send(user_id=user, message=message, random_id=0)
            # Выводим сообщение об успехе
            print(f"Сообщение отправлено пользователю {user} от аккаунта {login}")
    # Если возникла ошибка при авторизации
    except vk_api.AuthError as error:
        # Выводим сообщение об ошибке
        print(f"Не удалось авторизоваться от аккаунта {login}: {error}")
