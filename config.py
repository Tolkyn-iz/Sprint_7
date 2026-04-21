import random
import string

# URL конфигурация
BASE_URL = 'https://qa-scooter.praktikum-services.ru'

# Эндпоинты
COURIER_ENDPOINT = '/api/v1/courier'
LOGIN_ENDPOINT = '/api/v1/courier/login'
ORDERS_ENDPOINT = '/api/v1/orders'
ACCEPT_ORDER_ENDPOINT = '/api/v1/orders/accept'
CANCEL_ORDER_ENDPOINT = '/api/v1/orders/cancel'
GET_ORDER_ENDPOINT = '/api/v1/orders/track'

# Сообщения об ошибках
ERROR_MESSAGES = {
    'duplicate_login': "Этот логин уже используется. Попробуйте другой.",
    'insufficient_data': "Недостаточно данных для создания учетной записи",
    'login_not_found': "Учетная запись не найдена",
    'insufficient_login_data': "Недостаточно данных для входа",
    'courier_not_found': "Курьера с таким id нет.",
    'order_not_found': "Заказ не найден",
    'insufficient_search_data': "Недостаточно данных для поиска"
}

def generate_random_string(length):
    """Генерирует случайную строку из букв нижнего регистра"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))