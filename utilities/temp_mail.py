import requests
import re
from utilities.data import random_email, random_username
from settings import MailinatorConfig

api_token = MailinatorConfig.API_TOKEN


# Функция для получения последнего письма из Mailinator
def get_latest_email(random_username):
    global message_id
    random_username, domain = random_email.split('@')

    inbox_url = f"https://www.mailinator.com/api/v2/domains/private/inboxes/{random_username}"

    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    response = requests.get(inbox_url, headers=headers)
    if response.status_code == 200:
        message_id = response.json().get('msgs')[0].get('id')

    return message_id


# Функция для получения содержимого письма по ID
def get_email_content(username, message_id):
    message_url = f"https://www.mailinator.com/api/v2/domains/private/inboxes/{username}/messages/{message_id}"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    response = requests.get(message_url, headers=headers)

    if response.status_code == 200:
        return response.json().get("parts", [])[0].get("body", "")
    return None


# Получение последнего письма
def get_confirmation_link(browser):
    message_id = get_latest_email(random_email)
    email_content = get_email_content(random_username, message_id)
    # Поиск ссылки подтверждения в теле письма
    confirmation_link_match = re.search(r'https://[^\s"]+', email_content)
    confirmation_link = confirmation_link_match.group(0)
    print("Ссылка для подтверждения регистрации:", confirmation_link)
    return confirmation_link

    # message_id = get_latest_email(random_email)
    # if message_id:
    #     email_content = get_email_content(random_username, message_id)
    #     if email_content:
    #         # Поиск ссылки подтверждения в теле письма
    #         confirmation_link_match = re.search(r'https://[^\s"]+', email_content)
    #
    #         if confirmation_link_match:
    #             confirmation_link = confirmation_link_match.group(0)
    #             print("Ссылка для подтверждения регистрации:", confirmation_link)
    #
    #             # Переход по ссылке для подтверждения регистрации
    #             browser.get(confirmation_link)
    #             time.sleep(3)
    #
    #             # Ожидание успешного подтверждения
    #             WebDriverWait(browser, 10).until(
    #                 EC.text_to_be_present_in_element(
    #                     ConfirmEmailPageLocators.TEXT_EMAIL_CONFIRMED,
    #                     "Email confirmed."))
    #             print("Регистрация успешно подтверждена!")
    #         else:
    #             print("Ссылка на подтверждение не найдена в письме.")
    #     else:
    #         print("Не удалось получить содержимое письма.")
    # else:
    #     print("Не удалось получить ID последнего письма.")
