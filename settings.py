class Config:
    VALID_EMAIL_SELLER = "seller@gmail.com"
    VALID_EMAIL_SUPPLIER = "supplier@gmail.com"
    VALID_PASSWORD = "Password1!"
    INVALID_PASSWORD = "Qwerty123"
    INVALID_EMAIL = "sellergmail.com"
    # NONEXISTENT_EMAIL = "alesia@mail.ru"
    INVALID_REG_EMAILS = ['', 'example.com', 'user@', '@gmail.com', 'user!@example.com', 'user@invalid_domain',
                          'user@example.c', 'us er@example.com', 'user@@example.com', 'тест@gmail.com']

    invalid_reg_passwords = ['', 'Pass1*', 'PASSWORD2*', 'password3!', 'PassWord123',
                             'PassWord+!$', 'PassWord12&$', 'Пассворд1!']


class Urls:
    BASE_URL = 'https://dev.abra-market.com'
    LOGIN_URL = f'{BASE_URL}/login'
    REGISTER_URL = f'{BASE_URL}/register'
    CONFIRM_EMAIL_URL = f"{BASE_URL}/register/confirm_email"


class MailinatorConfig:
    API_TOKEN = "b6f16119855849afb525539046a3cab3"
    DOMAIN = "alesiateam.testinator.com"
