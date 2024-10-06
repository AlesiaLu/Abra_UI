import random
import string
from settings import MailinatorConfig


# Функция для генерации случайного email на Mailinator
def generate_random_email():
    domain = MailinatorConfig.DOMAIN
    username = 'qa_' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    email = f"{username}@{domain}"
    return email, username


random_email, random_username = generate_random_email()
print(f"Сгенерированный email: {random_email}")


# Генерация случайного пароля
def generate_random_password(length=8):
    if length < 8:
        raise ValueError("Длина пароля должна быть не менее 8 символов")
    # Обязательные символы
    lowercase_letter = random.choice(string.ascii_lowercase)
    capital_letter = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special_char = random.choice('!#*+$')
    # Оставшиеся символы
    other_chars = ''.join(random.choices(string.ascii_letters + string.digits + '!#*+$', k=length - 4))
    # Смешивание всех символов вместе
    password = lowercase_letter + capital_letter + digit + special_char + other_chars
    password = ''.join(random.sample(password, len(password)))  # Перемешивание символов
    return password


# Генерация пароля
random_password = generate_random_password(12)
print(f"Сгенерированный пароль: {random_password}")
